import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import re
import gzip

class SeoulFlightTracker:
    def __init__(self):
        """서울 항공기 추적기 초기화"""
        self.base_url = "https://seoul.flightfeeder.page/"
        self.driver = None

        # 항공기 기종 매핑 데이터베이스 (ICAO 코드 -> 실제 기종명)
        self.aircraft_types = {
            # Airbus
            'A319': 'Airbus A319',
            'A320': 'Airbus A320',
            'A321': 'Airbus A321',
            'A332': 'Airbus A330-200',
            'A333': 'Airbus A330-300',
            'A339': 'Airbus A330-900neo',
            'A342': 'Airbus A340-200',
            'A343': 'Airbus A340-300',
            'A346': 'Airbus A340-600',
            'A359': 'Airbus A350-900',
            'A35K': 'Airbus A350-1000',
            'A380': 'Airbus A380-800',
            'A388': 'Airbus A380-800',
            'A21N': 'Airbus A321neo',
            'A20N': 'Airbus A320neo',
            'A19N': 'Airbus A319neo',
            'A223': 'Airbus A220-300',
            'A221': 'Airbus A220-100',

            # Boeing
            'B712': 'Boeing 717-200',
            'B733': 'Boeing 737-300',
            'B734': 'Boeing 737-400',
            'B735': 'Boeing 737-500',
            'B736': 'Boeing 737-600',
            'B737': 'Boeing 737-700',
            'B738': 'Boeing 737-800',
            'B739': 'Boeing 737-900',
            'B38M': 'Boeing 737 MAX 8',
            'B39M': 'Boeing 737 MAX 9',
            'B3JM': 'Boeing 737 MAX 10',
            '737': 'Boeing 737',
            '738': 'Boeing 737-800',
            '739': 'Boeing 737-900',
            '7M8': 'Boeing 737 MAX 8',
            '7M9': 'Boeing 737 MAX 9',

            'B742': 'Boeing 747-200',
            'B743': 'Boeing 747-300',
            'B744': 'Boeing 747-400',
            'B748': 'Boeing 747-8',
            '744': 'Boeing 747-400',
            '748': 'Boeing 747-8',
            '74H': 'Boeing 747-8',

            'B752': 'Boeing 757-200',
            'B753': 'Boeing 757-300',
            'B762': 'Boeing 767-200',
            'B763': 'Boeing 767-300',
            'B764': 'Boeing 767-400',

            'B772': 'Boeing 777-200',
            'B77L': 'Boeing 777-200LR',
            'B773': 'Boeing 777-300',
            'B77W': 'Boeing 777-300ER',
            '772': 'Boeing 777-200ER',
            '773': 'Boeing 777-300',
            '77W': 'Boeing 777-300ER',

            'B787': 'Boeing 787',
            'B788': 'Boeing 787-8',
            'B789': 'Boeing 787-9',
            'B78X': 'Boeing 787-10',
            '787': 'Boeing 787',
            '788': 'Boeing 787-8',
            '789': 'Boeing 787-9',
            '78X': 'Boeing 787-10',

            # Embraer
            'E145': 'Embraer ERJ-145',
            'E170': 'Embraer E170',
            'E175': 'Embraer E175',
            'E190': 'Embraer E190',
            'E195': 'Embraer E195',
            'E290': 'Embraer E190-E2',

            # ATR
            'AT72': 'ATR 72',
            'AT76': 'ATR 72-600',
            'AT45': 'ATR 42-500',

            # Other common types
            'DH8D': 'Bombardier Dash 8 Q400',
            'DH8C': 'Bombardier Dash 8 Q300',
            'CRJ2': 'Bombardier CRJ-200',
            'CRJ7': 'Bombardier CRJ-700',
            'CRJ9': 'Bombardier CRJ-900',
            'C25A': 'Cessna Citation CJ2',
            'C25B': 'Cessna Citation CJ3',
            'C56X': 'Cessna Citation Excel',
            'C680': 'Cessna Citation Latitude'
        }

        # 항공사 코드 매핑
        self.airline_codes = {
            'KAL': 'Korean Air',
            'AAR': 'Asiana Airlines',
            'ABL': 'Air Busan',
            'ASV': 'Air Seoul',
            'JJA': 'Jeju Air',
            'TWB': "T'way Air",
            'ESR': 'Eastar Jet',
            'FGW': 'Fly Gangwon',
            'JNA': 'Jin Air',
            'LCC': 'Low Cost Carrier'
        }

        # ICAO hex 코드를 통한 항공기 정보 매핑 (데이터베이스에서 로드)
        self.icao_to_aircraft = {}

    def get_aircraft_type_info(self, type_code, hex_code=None):
        """항공기 타입 코드와 ICAO hex를 통해 실제 기종명으로 변환"""

        # 1. ICAO hex 코드로 데이터베이스에서 조회 (가장 정확)
        if hex_code and hex_code.lower() in self.icao_to_aircraft:
            aircraft_info = self.icao_to_aircraft[hex_code.lower()]
            full_name = f"{aircraft_info['manufacturer']} {aircraft_info['model']}".strip()
            print(f"🎯 ICAO hex {hex_code}로 데이터베이스에서 발견: {full_name} ({aircraft_info['type']})")
            return {
                'type_code': aircraft_info['type'],
                'manufacturer': aircraft_info['manufacturer'],
                'model': aircraft_info['model'],
                'full_name': full_name
            }

        # 2. 기존 로직 계속 사용
        if not type_code or pd.isna(type_code):
            return {'type_code': None, 'manufacturer': 'Unknown', 'model': 'Unknown', 'full_name': 'Unknown'}

        # 문자열로 변환하고 정리
        type_code = str(type_code).upper().strip()

        # 빈 문자열이나 의미없는 값 체크
        if not type_code or type_code in ['', 'NAN', 'NONE', 'NULL', 'ADSB_ICAO', 'MODE_S', 'MLAT']:
            return {'type_code': type_code, 'manufacturer': 'Unknown', 'model': 'Unknown', 'full_name': f'Unknown ({type_code})'}

        print(f"🔍 기종 코드 분석: '{type_code}' (hex: {hex_code})")

        # 3. 직접 매핑에서 찾기
        if type_code in self.aircraft_types:
            full_name = self.aircraft_types[type_code]
            manufacturer, model = self._parse_aircraft_name(full_name)
            print(f"  ✅ 직접 매핑 발견: {full_name}")
            return {
                'type_code': type_code,
                'manufacturer': manufacturer,
                'model': model,
                'full_name': full_name
            }

        # 4. 부분 매핑 시도
        for known_code, full_name in self.aircraft_types.items():
            if type_code.startswith(known_code) or known_code.startswith(type_code):
                manufacturer, model = self._parse_aircraft_name(full_name)
                print(f"  ✅ 부분 매핑 발견: {type_code} ≈ {known_code} → {full_name}")
                return {
                    'type_code': type_code,
                    'manufacturer': manufacturer,
                    'model': model,
                    'full_name': full_name
                }

        # 5. 패턴 기반 분석
        aircraft_info = self._analyze_type_pattern(type_code)
        if aircraft_info['manufacturer'] != 'Unknown':
            print(f"  ✅ 패턴 분석 성공: {aircraft_info['full_name']}")
            return aircraft_info

        # 6. 추론
        inferred_info = self._infer_aircraft_type(type_code)
        if inferred_info['manufacturer'] != 'Unknown':
            print(f"  ✅ 추론 성공: {inferred_info['full_name']}")
            return inferred_info

        print(f"  ❌ 매핑 실패, Unknown으로 설정")
        return {
            'type_code': type_code,
            'manufacturer': 'Unknown',
            'model': type_code,
            'full_name': f'Unknown ({type_code})'
        }

    def _parse_aircraft_name(self, full_name):
        """전체 기종명에서 제조사와 모델 분리"""
        if 'Airbus' in full_name:
            manufacturer = 'Airbus'
            model = full_name.replace('Airbus ', '')
        elif 'Boeing' in full_name:
            manufacturer = 'Boeing'
            model = full_name.replace('Boeing ', '')
        elif 'Embraer' in full_name:
            manufacturer = 'Embraer'
            model = full_name.replace('Embraer ', '')
        elif 'Bombardier' in full_name:
            manufacturer = 'Bombardier'
            model = full_name.replace('Bombardier ', '')
        elif 'ATR' in full_name:
            manufacturer = 'ATR'
            model = full_name.replace('ATR ', '')
        else:
            parts = full_name.split(' ')
            manufacturer = parts[0] if parts else 'Unknown'
            model = ' '.join(parts[1:]) if len(parts) > 1 else full_name

        return manufacturer, model

    def _analyze_type_pattern(self, type_code):
        """패턴 분석으로 항공기 추정"""
        type_code = type_code.upper()

        # Airbus 패턴
        if re.match(r'^A\d{3}', type_code):
            model_match = re.match(r'^A(\d{3})(.*)$', type_code)
            if model_match:
                model_num = model_match.group(1)
                variant = model_match.group(2)
                full_name = f'Airbus A{model_num}{variant}'
                return {
                    'type_code': type_code,
                    'manufacturer': 'Airbus',
                    'model': f'A{model_num}{variant}',
                    'full_name': full_name
                }

        # Boeing 패턴
        boeing_patterns = [
            r'^B(\d{3})(.*)$',
            r'^(\d{3})(.*)$',
            r'^7(\d{2})(.*)$'
        ]

        for pattern in boeing_patterns:
            match = re.match(pattern, type_code)
            if match:
                if pattern.startswith('^7'):
                    model_num = '7' + match.group(1)
                else:
                    model_num = match.group(1)

                variant = match.group(2) if len(match.groups()) > 1 else ''

                if model_num in ['737', '747', '757', '767', '777', '787']:
                    full_name = f'Boeing {model_num}{variant}'
                    return {
                        'type_code': type_code,
                        'manufacturer': 'Boeing',
                        'model': f'{model_num}{variant}',
                        'full_name': full_name
                    }

        return {
            'type_code': type_code,
            'manufacturer': 'Unknown',
            'model': type_code,
            'full_name': type_code
        }

    def _infer_aircraft_type(self, type_code):
        """간단한 추론을 통한 항공기 타입 추정"""
        type_code = type_code.upper()

        if len(type_code) >= 3:
            if type_code.startswith('A'):
                return {
                    'type_code': type_code,
                    'manufacturer': 'Airbus',
                    'model': type_code,
                    'full_name': f'Airbus {type_code}'
                }
            elif type_code.startswith('B') or type_code[0].isdigit():
                return {
                    'type_code': type_code,
                    'manufacturer': 'Boeing',
                    'model': type_code,
                    'full_name': f'Boeing {type_code}'
                }
            elif type_code.startswith('E'):
                return {
                    'type_code': type_code,
                    'manufacturer': 'Embraer',
                    'model': type_code,
                    'full_name': f'Embraer {type_code}'
                }

        return {
            'type_code': type_code,
            'manufacturer': 'Unknown',
            'model': type_code,
            'full_name': type_code
        }

    def get_airline_name(self, callsign_or_code):
        """콜사인이나 코드를 통해 항공사명 추정"""
        if not callsign_or_code:
            return 'Unknown'

        code = str(callsign_or_code).upper().strip()

        # 직접 매핑
        if code in self.airline_codes:
            return self.airline_codes[code]

        # 콜사인 패턴으로 추정
        if code.startswith('KAL'):
            return 'Korean Air'
        elif code.startswith('AAR'):
            return 'Asiana Airlines'
        elif code.startswith('JJA'):
            return 'Jeju Air'
        elif code.startswith('TWB'):
            return "T'way Air"
        elif code.startswith('ABL'):
            return 'Air Busan'
        elif code.startswith('ASV'):
            return 'Air Seoul'

        return code

    def setup_driver(self, headless=True):
        """Selenium 웹드라이버 설정"""
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        return self.driver

    def get_aircraft_data_selenium(self):
        """Selenium을 사용하여 항공기 데이터 수집"""
        if not self.driver:
            self.setup_driver()

        try:
            print("🌐 웹페이지 로딩 중...")
            self.driver.get(self.base_url)
            time.sleep(8)

            aircraft_data = []

            # JavaScript 변수에서 데이터 추출 시도
            print("🔍 JavaScript 변수 확인 중...")
            js_variables = [
                "window.aircraft",
                "window.aircraftDatabase",
                "window.Planes",
                "window.aircraftList",
                "window.planelist",
                "window.data",
                "aircraft",
                "aircraftDatabase",
                "Planes",
                "aircraftList",
                "planelist",
                "AircraftDatabase"
            ]

            for var in js_variables:
                try:
                    script = f"return (typeof {var} !== 'undefined') ? {var} : null;"
                    data = self.driver.execute_script(script)
                    if data and isinstance(data, (list, dict)):
                        print(f"✅ JavaScript 변수 '{var}'에서 데이터 발견: {type(data)}")
                        if isinstance(data, list) and len(data) > 0:
                            print(f"   데이터 개수: {len(data)}개")
                        aircraft_data = data
                        break
                except Exception as e:
                    continue

            # 페이지 소스에서 JSON 패턴 찾기
            if not aircraft_data:
                print("🔍 페이지 소스에서 JSON 데이터 검색 중...")
                page_source = self.driver.page_source

                json_patterns = [
                    r'aircraft[\s]*=[\s]*(\[.*?\]);',
                    r'aircraftList[\s]*=[\s]*(\[.*?\]);',
                    r'planes[\s]*=[\s]*(\[.*?\]);',
                    r'"aircraft"[\s]*:[\s]*(\[.*?\])',
                    r'var\s+\w+\s*=\s*(\[.*?\]);'
                ]

                for pattern in json_patterns:
                    matches = re.findall(pattern, page_source, re.DOTALL | re.IGNORECASE)
                    for match in matches:
                        try:
                            data = json.loads(match)
                            if isinstance(data, list) and len(data) > 0:
                                print(f"✅ 페이지 소스에서 JSON 데이터 발견: {len(data)}개 항공기")
                                aircraft_data = data
                                break
                        except:
                            continue
                    if aircraft_data:
                        break

            # DOM에서 테이블 데이터 추출 시도
            if not aircraft_data:
                print("🔍 DOM 테이블에서 데이터 추출 시도...")
                table_selectors = [
                    "table tbody tr",
                    ".aircraft-table tbody tr",
                    "#aircraftTable tbody tr",
                    "table tr"
                ]

                for selector in table_selectors:
                    try:
                        rows = self.driver.find_elements(By.CSS_SELECTOR, selector)
                        if rows and len(rows) > 1:
                            print(f"✅ 테이블 발견: {len(rows)}개 행")

                            for row in rows[1:]:
                                cells = row.find_elements(By.TAG_NAME, "td")
                                if cells:
                                    row_data = {}
                                    for i, cell in enumerate(cells):
                                        row_data[f'col_{i}'] = cell.text.strip()
                                    aircraft_data.append(row_data)

                            if aircraft_data:
                                print(f"✅ DOM에서 {len(aircraft_data)}개 항공기 데이터 추출")
                                break

                    except Exception as e:
                        continue

            # 네트워크 로그 확인
            api_calls = []
            try:
                logs = self.driver.get_log('performance')
                for log in logs:
                    try:
                        message = json.loads(log['message'])
                        if message.get('message', {}).get('method') == 'Network.responseReceived':
                            url = message['message']['params']['response']['url']
                            if any(keyword in url.lower() for keyword in ['aircraft', 'data', 'json', 'api']):
                                api_calls.append(url)
                    except:
                        continue

                if api_calls:
                    print(f"🔍 발견된 API 호출: {len(api_calls)}개")
                    for api_call in api_calls[:5]:
                        print(f"  - {api_call}")

            except Exception as e:
                print(f"네트워크 로그 확인 중 오류: {e}")

            return {
                'aircraft_data': aircraft_data,
                'api_calls': api_calls,
                'page_source_length': len(self.driver.page_source) if self.driver else 0
            }

        except Exception as e:
            print(f"❌ 데이터 수집 중 오류 발생: {e}")
            return None

        finally:
            if self.driver:
                self.driver.quit()
                self.driver = None

    def try_api_endpoints(self):
        """항공기 추적 API 엔드포인트들을 시도"""

        # API 엔드포인트들
        api_endpoints = [
            "https://seoul.flightfeeder.page/data/aircraft.json",
            "https://seoul.flightfeeder.page/data/receiver.json",
            "https://seoul.flightfeeder.page/api/aircraft",
            "https://seoul.flightfeeder.page/data.json",
            "https://seoul.flightfeeder.page/aircraft.json",
            "https://seoul.flightfeeder.page/dump1090/data/aircraft.json",
            "https://seoul.flightfeeder.page/dump1090-fa/data/aircraft.json",
            "https://seoul.flightfeeder.page/tar1090/data/aircraft.json"
        ]

        # 항공기 데이터베이스 URL도 시도
        database_endpoints = [
            "https://seoul.flightfeeder.page/db/aircraft.csv.gz",
            "https://seoul.flightfeeder.page/data/aircraft.csv.gz",
            "https://seoul.flightfeeder.page/tar1090/aircraft.csv.gz"
        ]

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://seoul.flightfeeder.page/',
            'Accept': 'application/json, text/plain, */*'
        }

        # 항공기 데이터베이스 다운로드 시도
        for db_endpoint in database_endpoints:
            try:
                print(f"🗄️ 항공기 DB 요청: {db_endpoint}")
                response = requests.get(db_endpoint, headers=headers, timeout=15)
                if response.status_code == 200:
                    print(f"✅ 항공기 데이터베이스 발견")
                    self._load_aircraft_database(response.content)
                    break
            except Exception as e:
                print(f"❌ DB 요청 실패: {e}")

        # 실시간 항공기 데이터 요청
        for endpoint in api_endpoints:
            try:
                print(f"🌐 API 요청: {endpoint}")
                response = requests.get(endpoint, headers=headers, timeout=15)

                if response.status_code == 200:
                    try:
                        data = response.json()
                        print(f"✅ API 성공: {endpoint}")

                        if isinstance(data, dict) and 'aircraft' in data:
                            aircraft_count = len(data['aircraft']) if isinstance(data['aircraft'], list) else 0
                            print(f"   항공기 수: {aircraft_count}개")
                        elif isinstance(data, list):
                            print(f"   항목 수: {len(data)}")

                        return data

                    except json.JSONDecodeError as e:
                        print(f"⚠️ JSON 파싱 실패: {e}")
                else:
                    print(f"❌ HTTP {response.status_code}")

            except requests.RequestException as e:
                print(f"❌ 요청 실패: {e}")

            time.sleep(0.5)

        return None

    def _load_aircraft_database(self, db_content):
        """항공기 데이터베이스 로드 및 파싱"""
        try:
            # gzip 압축 해제
            decompressed_data = gzip.decompress(db_content)
            csv_data = decompressed_data.decode('utf-8')

            print("🗄️ 항공기 데이터베이스 로딩 중...")

            # CSV 파싱 - 세미콜론으로 구분된 CSV 파일
            lines = csv_data.strip().split('\n')
            db_count = 0

            for line_num, line in enumerate(lines):
                if not line.strip():
                    continue

                try:
                    # 세미콜론으로 분리
                    parts = line.split(';')
                    if len(parts) >= 5:  # 최소 5개 컬럼 필요
                        icao_hex = parts[0].strip().lower()
                        registration = parts[1].strip()
                        aircraft_type = parts[2].strip()
                        aircraft_name = parts[4].strip() if len(parts) > 4 else ''

                        if icao_hex and aircraft_type:
                            self.icao_to_aircraft[icao_hex] = {
                                'type': aircraft_type,
                                'registration': registration,
                                'name': aircraft_name,
                                'manufacturer': self._get_manufacturer_from_type(aircraft_type),
                                'model': self._get_model_from_type(aircraft_type)
                            }
                            db_count += 1

                except Exception as e:
                    # 파싱 오류가 있는 라인은 건너뛰기
                    continue

            print(f"✅ 데이터베이스 로드 완료: {db_count:,}개 항공기")

            # 샘플 데이터 출력
            if db_count > 0:
                sample_keys = list(self.icao_to_aircraft.keys())[:3]
                print("📋 샘플 데이터:")
                for key in sample_keys:
                    info = self.icao_to_aircraft[key]
                    print(f"  {key.upper()}: {info['manufacturer']} {info['model']} ({info['type']})")

        except Exception as e:
            print(f"⚠️ 데이터베이스 로드 실패: {e}")
            self.icao_to_aircraft = {}

    def _get_manufacturer_from_type(self, aircraft_type):
        """항공기 타입에서 제조사 추출"""
        if not aircraft_type:
            return "Unknown"

        type_upper = aircraft_type.upper()

        # Airbus 패턴 (더 포괄적)
        if any(pattern in type_upper for pattern in ['A31', 'A32', 'A33', 'A34', 'A35', 'A38', 'A19N', 'A20N', 'A21N', 'A22']):
            return "Airbus"
        # Boeing 패턴 (더 포괄적)
        elif any(pattern in type_upper for pattern in ['B73', 'B74', 'B75', 'B76', 'B77', 'B78', '737', '747', '757', '767', '777', '787', '7M8', '7M9']):
            return "Boeing"
        # Embraer 패턴
        elif type_upper.startswith('E1') or type_upper.startswith('E2') or 'ERJ' in type_upper:
            return "Embraer"
        # ATR 패턴
        elif type_upper.startswith('AT') or 'ATR' in type_upper:
            return "ATR"
        # Bombardier 패턴
        elif 'CRJ' in type_upper or 'DH8' in type_upper or 'DASH' in type_upper:
            return "Bombardier"
        # Cessna 패턴
        elif type_upper.startswith('C') and any(pattern in type_upper for pattern in ['25', '56', '68', '172', '208']):
            return "Cessna"
        # 기타 알려진 제조사들
        elif 'BE' in type_upper[:3]:
            return "Beechcraft"
        else:
            return "Unknown"

    def _get_model_from_type(self, aircraft_type):
        """항공기 타입에서 모델 추출"""
        if not aircraft_type:
            return "Unknown"

        # 먼저 내부 매핑 테이블에서 찾기
        if aircraft_type in self.aircraft_types:
            return self.aircraft_types[aircraft_type].split(' ', 1)[-1]

        # 타입 코드를 더 친숙한 이름으로 변환
        type_upper = aircraft_type.upper()

        if type_upper == 'A20N':
            return "A320neo"
        elif type_upper == 'A21N':
            return "A321neo"
        elif type_upper == 'A19N':
            return "A319neo"
        elif type_upper == 'B38M' or type_upper == '7M8':
            return "737 MAX 8"
        elif type_upper == 'B39M' or type_upper == '7M9':
            return "737 MAX 9"
        elif type_upper == 'B732':
            return "737-200"
        elif type_upper == 'B737' or type_upper == '737':
            return "737-700"
        elif type_upper == 'B738' or type_upper == '738':
            return "737-800"
        elif type_upper == 'B789' or type_upper == '789':
            return "787-9"
        elif type_upper == 'B788' or type_upper == '788':
            return "787-8"
        elif type_upper == 'B77W' or type_upper == '77W':
            return "777-300ER"
        elif type_upper == 'A333':
            return "A330-300"
        elif type_upper == 'A332':
            return "A330-200"
        elif type_upper == 'A359':
            return "A350-900"

        return aircraft_type

    def _load_external_aircraft_database(self):
        """외부 항공기 데이터베이스 로드"""
        try:
            db_urls = [
                "https://github.com/wiedehopf/tar1090-db/raw/csv/aircraft.csv.gz",
                "https://raw.githubusercontent.com/Mictronics/readsb/dev/webapp/src/db/aircraft.csv.gz"
            ]

            for db_url in db_urls:
                try:
                    print(f"🌐 외부 DB 다운로드: {db_url}")
                    response = requests.get(db_url, timeout=30)

                    if response.status_code == 200:
                        print(f"✅ 외부 데이터베이스 다운로드 성공")
                        self._load_aircraft_database(response.content)
                        return True

                except Exception as e:
                    print(f"❌ 다운로드 실패: {e}")
                    continue

            print("❌ 모든 외부 데이터베이스 다운로드 실패")
            return False

        except Exception as e:
            print(f"❌ 외부 데이터베이스 로드 오류: {e}")
            return False

    def format_aircraft_data(self, raw_data):
        """항공기 데이터를 DataFrame으로 변환하고 기종 정보 추가"""
        if not raw_data:
            return None

        # 데이터 구조에 따라 파싱
        aircraft_list = []

        if isinstance(raw_data, dict):
            if 'aircraft' in raw_data:
                aircraft_list = raw_data['aircraft']
            elif 'planes' in raw_data:
                aircraft_list = raw_data['planes']
            else:
                aircraft_list = [raw_data]
        elif isinstance(raw_data, list):
            aircraft_list = raw_data

        if not aircraft_list:
            return None

        # DataFrame 생성
        df = pd.DataFrame(aircraft_list)

        # 원본 데이터 구조 디버깅
        print("🔍 원본 데이터 구조:")
        print(f"컬럼들: {list(df.columns)}")
        if not df.empty:
            print("샘플 데이터 (첫 번째 행):")
            for col in df.columns[:10]:  # 처음 10개만
                print(f"  {col}: {df[col].iloc[0] if not df[col].empty else 'N/A'}")

        # 확장된 컬럼명 매핑
        column_mapping = {
            # 식별 정보
            'hex': '식별코드',
            'icao': '식별코드',
            'addr': '식별코드',

            # 편명/콜사인
            'flight': '편명',
            'callsign': '편명',
            'call': '편명',
            'ident': '편명',

            # 등록번호
            'r': '등록번호',
            'reg': '등록번호',
            'registration': '등록번호',

            # 기종 코드
            't': '기종코드',
            'type': '기종코드',
            'aircraft_type': '기종코드',
            'ac_type': '기종코드',
            'typeCode': '기종코드',
            'typ': '기종코드',

            # 위치 정보
            'lat': '위도',
            'latitude': '위도',
            'lon': '경도',
            'lng': '경도',
            'longitude': '경도',

            # 고도 정보
            'altitude': '고도',
            'alt': '고도',
            'alt_baro': '기압고도',
            'baro_altitude': '기압고도',
            'alt_geom': 'GPS고도',
            'geom_altitude': 'GPS고도',

            # 속도/방향
            'gs': '지상속도',
            'ground_speed': '지상속도',
            'speed': '지상속도',
            'track': '방향',
            'heading': '방향',
            'true_track': '방향',

            # 기타 정보
            'squawk': '스쿼크',
            'code': '스쿼크',
            'baro_rate': '상승률',
            'vert_rate': '상승률',
            'vertical_rate': '상승률',
            'category': '카테고리',
            'emergency': '비상상황',
            'spi': 'SPI',
            'mlat': 'MLAT',
            'tisb': 'TIS-B',
            'messages': '메시지수',
            'msgs': '메시지수',
            'seen': '마지막수신',
            'seen_pos': '위치수신',
            'rssi': '신호강도',
            'nucp': 'NUCP',
            'nacp': 'NACP'
        }

        # 컬럼명 변경
        df = df.rename(columns=column_mapping)

        # 기종 코드 컬럼 찾기
        type_code_column = None
        for possible_col in ['기종코드', 't', 'type', 'aircraft_type', 'ac_type']:
            if possible_col in df.columns:
                type_code_column = possible_col
                break

        # 매핑 후에도 기종코드가 없다면 원본에서 찾기
        if type_code_column is None:
            for col in df.columns:
                if any(keyword in col.lower() for keyword in ['type', 'aircraft', 'plane']):
                    df = df.rename(columns={col: '기종코드'})
                    type_code_column = '기종코드'
                    break

        print(f"🔍 사용할 기종코드 컬럼: {type_code_column}")

        # 기종 정보 추가 처리
        if type_code_column and type_code_column in df.columns:
            print("✅ 기종 정보 매핑 시작...")
            aircraft_info_list = []

            # hex 코드 컬럼 찾기
            hex_column = None
            for col in ['식별코드', 'hex', 'icao', 'addr']:
                if col in df.columns:
                    hex_column = col
                    break

            for idx, row in df.iterrows():
                type_code = row[type_code_column]
                hex_code = row[hex_column] if hex_column else None

                print(f"  행 {idx}: 기종코드='{type_code}', hex='{hex_code}'")

                aircraft_info = self.get_aircraft_type_info(type_code, hex_code)
                print(f"  → 매핑 결과: {aircraft_info['manufacturer']} {aircraft_info['model']}")
                aircraft_info_list.append(aircraft_info)

            # 새로운 컬럼들 추가
            aircraft_info_df = pd.DataFrame(aircraft_info_list)
            df['제조사'] = aircraft_info_df['manufacturer']
            df['기종'] = aircraft_info_df['model']
            df['기종명'] = aircraft_info_df['full_name']

            # 디버깅: 매핑 결과 확인
            print("\n📊 기종 매핑 결과:")
            if not df.empty:
                for i, row in df.head().iterrows():
                    print(f"  행 {i}: {row.get(type_code_column, 'N/A')} → {row.get('제조사', 'N/A')} {row.get('기종', 'N/A')}")

        else:
            print("⚠️ 기종 코드 컬럼을 찾을 수 없습니다.")
            df['제조사'] = 'Unknown'
            df['기종'] = 'Unknown'
            df['기종명'] = 'Unknown'

        # 항공사 정보 추가
        callsign_column = None
        for col in ['편명', 'flight', 'callsign', 'call', 'ident']:
            if col in df.columns:
                callsign_column = col
                break

        if callsign_column:
            print(f"✅ 항공사 정보 매핑 (컬럼: {callsign_column})...")
            df['항공사'] = df[callsign_column].apply(self.get_airline_name)
        else:
            df['항공사'] = 'Unknown'

        # 컬럼 순서 재정렬
        preferred_columns = ['편명', '항공사', '제조사', '기종', '기종명', '등록번호',
                           '고도', '지상속도', '위도', '경도', '방향', '스쿼크']

        available_preferred = [col for col in preferred_columns if col in df.columns]
        other_columns = [col for col in df.columns if col not in preferred_columns]

        if available_preferred:
            df = df[available_preferred + other_columns]

        return df

    def test_data_sources(self):
        """모든 데이터 소스 테스트 및 디버깅"""
        print("🧪 데이터 소스 테스트 시작...")
        print("=" * 60)

        # 1. API 엔드포인트 테스트
        print("\n1️⃣ API 엔드포인트 테스트")
        api_data = self.try_api_endpoints()

        if api_data:
            print("✅ API 테스트 성공")
            df = self.format_aircraft_data(api_data)
            if df is not None and not df.empty:
                print(f"   변환된 DataFrame: {len(df)}행 x {len(df.columns)}열")
                return df
        else:
            print("❌ API 테스트 실패")

        # 2. Selenium 테스트
        print("\n2️⃣ Selenium 브라우저 테스트")
        selenium_result = self.get_aircraft_data_selenium()

        if selenium_result and selenium_result['aircraft_data']:
            print("✅ Selenium 테스트 성공")
            df = self.format_aircraft_data(selenium_result['aircraft_data'])
            if df is not None and not df.empty:
                print(f"   변환된 DataFrame: {len(df)}행 x {len(df.columns)}열")
                return df
        else:
            print("❌ Selenium 테스트 실패")

        # 3. 발견된 API 호출들로 재시도
        if selenium_result and selenium_result['api_calls']:
            print("\n3️⃣ 발견된 API 호출로 재시도")
            for api_url in selenium_result['api_calls'][:3]:
                try:
                    print(f"🌐 재시도: {api_url}")
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                        'Referer': 'https://seoul.flightfeeder.page/'
                    }
                    response = requests.get(api_url, headers=headers, timeout=10)

                    if response.status_code == 200:
                        try:
                            data = response.json()
                            print(f"✅ 재시도 성공: {api_url}")
                            df = self.format_aircraft_data(data)
                            if df is not None and not df.empty:
                                return df
                        except:
                            continue
                except:
                    continue

        print("\n❌ 모든 데이터 소스 테스트 실패")
        return None

    def get_flight_data(self):
        """통합 데이터 수집 메서드"""
        print("🛫 서울 지역 항공기 데이터 수집 시작...")
        print("=" * 50)

        # 외부 항공기 데이터베이스 먼저 로드 시도
        print("🗄️ 항공기 데이터베이스 준비 중...")
        if not hasattr(self, 'icao_to_aircraft') or not self.icao_to_aircraft:
            self._load_external_aircraft_database()

        # 디버깅 모드로 모든 소스 테스트
        df = self.test_data_sources()

        if df is not None and not df.empty:
            print(f"\n🎉 데이터 수집 성공!")
            print(f"📊 수집된 데이터 요약:")
            print(f"  - 항공기 수: {len(df)}대")
            print(f"  - 컬럼 수: {len(df.columns)}개")

            # 기종 매핑 상태 확인
            if '제조사' in df.columns:
                manufacturer_counts = df['제조사'].value_counts()
                print(f"  - 제조사 매핑 결과:")
                for mfg, count in manufacturer_counts.items():
                    print(f"    * {mfg}: {count}대")

                # 성공률 계산
                unknown_count = manufacturer_counts.get('Unknown', 0)
                total_count = len(df)
                success_rate = ((total_count - unknown_count) / total_count * 100) if total_count > 0 else 0

                print(f"\n📈 기종 식별 성공률: {success_rate:.1f}% ({total_count - unknown_count}/{total_count})")

                if unknown_count > 0:
                    print(f"⚠️ {unknown_count}개 항공기의 기종을 식별하지 못했습니다.")
                    if '기종코드' in df.columns:
                        unknown_codes = df[df['제조사'] == 'Unknown']['기종코드'].value_counts().head(5)
                        print("   미식별 기종코드 TOP 5:")
                        for code, count in unknown_codes.items():
                            print(f"    * '{code}': {count}개")

            return df
        else:
            print("\n❌ 모든 방법으로 데이터를 가져올 수 없습니다.")
            print("\n💡 문제 해결 방법:")
            print("1. 인터넷 연결 상태를 확인하세요")
            print("2. 사이트가 일시적으로 접근 불가능할 수 있습니다")
            print("3. VPN 사용을 시도해보세요")
            print("4. Chrome 브라우저가 정상적으로 설치되어 있는지 확인하세요")

            return None

# 사용 예제 및 추가 분석 함수들
def analyze_aircraft_data(df):
    """항공기 데이터 상세 분석"""
    if df is None or df.empty:
        print("분석할 데이터가 없습니다.")
        return

    print("\n🔍 상세 분석 결과:")
    print("=" * 50)

    # Boeing vs Airbus 비교
    if '제조사' in df.columns:
        boeing_count = len(df[df['제조사'] == 'Boeing'])
        airbus_count = len(df[df['제조사'] == 'Airbus'])
        total_count = len(df[df['제조사'].isin(['Boeing', 'Airbus'])])

        if total_count > 0:
            print(f"\n✈️ Boeing vs Airbus:")
            print(f"  - Boeing: {boeing_count}대 ({boeing_count/total_count*100:.1f}%)")
            print(f"  - Airbus: {airbus_count}대 ({airbus_count/total_count*100:.1f}%)")

    # 가장 많이 사용되는 기종 TOP 5
    if '기종명' in df.columns:
        print(f"\n🏆 가장 많이 운항 중인 기종 TOP 5:")
        top_aircraft = df['기종명'].value_counts().head(5)
        for i, (aircraft, count) in enumerate(top_aircraft.items(), 1):
            if 'Unknown' not in aircraft:
                print(f"  {i}. {aircraft}: {count}대")

    # 고도 구간별 분포
    if '고도' in df.columns:
        altitude_data = df[df['고도'].notna()]
        if not altitude_data.empty:
            print(f"\n🏔️ 고도 구간별 분포:")

            altitude_ranges = [
                (0, 10000, "저고도 (0-10,000ft)"),
                (10000, 25000, "중고도 (10,000-25,000ft)"),
                (25000, 40000, "고고도 (25,000-40,000ft)"),
                (40000, float('inf'), "초고고도 (40,000ft+)")
            ]

            for min_alt, max_alt, range_name in altitude_ranges:
                count = len(altitude_data[
                    (altitude_data['고도'] >= min_alt) &
                    (altitude_data['고도'] < max_alt)
                ])
                if count > 0:
                    print(f"  - {range_name}: {count}대")

def get_aircraft_by_type(df, aircraft_type):
    """특정 기종의 항공기만 필터링"""
    if df is None or df.empty:
        return None

    aircraft_type = aircraft_type.upper()

    filtered_df = df[
        (df.get('기종', '').str.contains(aircraft_type, na=False, case=False)) |
        (df.get('기종명', '').str.contains(aircraft_type, na=False, case=False)) |
        (df.get('제조사', '').str.contains(aircraft_type, na=False, case=False))
    ]

    return filtered_df if not filtered_df.empty else None

def get_korean_airlines_only(df):
    """한국 항공사 항공기만 필터링"""
    if df is None or df.empty:
        return None

    korean_airlines = ['Korean Air', 'Asiana Airlines', 'Jeju Air', "T'way Air",
                      'Air Busan', 'Air Seoul', 'Jin Air', 'Eastar Jet', 'Fly Gangwon']

    if '항공사' in df.columns:
        korean_df = df[df['항공사'].isin(korean_airlines)]
        return korean_df if not korean_df.empty else None

    return None

def search_by_flight_number(df, flight_number):
    """편명으로 항공기 검색"""
    if df is None or df.empty or '편명' not in df.columns:
        return None

    flight_number = flight_number.upper()
    result = df[df['편명'].str.contains(flight_number, na=False, case=False)]
    return result if not result.empty else None

def get_high_altitude_aircraft(df, min_altitude=30000):
    """고고도 비행 중인 항공기 조회"""
    if df is None or df.empty or '고도' not in df.columns:
        return None

    high_alt = df[df['고도'] >= min_altitude]
    return high_alt if not high_alt.empty else None

def get_aircraft_summary_stats(df):
    """항공기 데이터 요약 통계"""
    if df is None or df.empty:
        return None

    stats = {
        '총_항공기수': len(df),
        '제조사별': df.get('제조사', pd.Series()).value_counts().to_dict() if '제조사' in df.columns else {},
        '항공사별': df.get('항공사', pd.Series()).value_counts().to_dict() if '항공사' in df.columns else {},
        '기종별': df.get('기종명', pd.Series()).value_counts().head(10).to_dict() if '기종명' in df.columns else {}
    }

    if '고도' in df.columns:
        altitude_data = df[df['고도'].notna()]
        if not altitude_data.empty:
            stats['고도_통계'] = {
                '평균': float(altitude_data['고도'].mean()),
                '최대': float(altitude_data['고도'].max()),
                '최소': float(altitude_data['고도'].min()),
                '표준편차': float(altitude_data['고도'].std())
            }

    if '지상속도' in df.columns:
        speed_data = df[df['지상속도'].notna()]
        if not speed_data.empty:
            stats['속도_통계'] = {
                '평균': float(speed_data['지상속도'].mean()),
                '최대': float(speed_data['지상속도'].max()),
                '최소': float(speed_data['지상속도'].min())
            }

    return stats

def main():
    """메인 실행 함수"""
    tracker = SeoulFlightTracker()

    try:
        # 데이터 수집
        df = tracker.get_flight_data()

        if df is not None and not df.empty:
            print(f"\n✅ 총 {len(df)}개의 항공기 데이터 수집 완료!")
            print("\n📊 수집된 데이터:")
            print(df.to_string(index=False))

            # CSV 파일로 저장
            df.to_csv('seoul_aircraft_data.csv', index=False, encoding='utf-8-sig')
            print(f"\n💾 데이터가 'seoul_aircraft_data.csv' 파일로 저장되었습니다.")

            # 기본 통계 정보
            print(f"\n📈 통계 정보:")
            print(f"  - 전체 항공기 수: {len(df)}")

            if '제조사' in df.columns:
                print(f"  - 제조사별 분포:")
                manufacturer_counts = df['제조사'].value_counts()
                for manufacturer, count in manufacturer_counts.items():
                    print(f"    * {manufacturer}: {count}대")

            if '기종' in df.columns:
                print(f"  - 기종별 분포:")
                model_counts = df['기종'].value_counts().head(10)
                for model, count in model_counts.items():
                    if 'Unknown' not in model:
                        print(f"    * {model}: {count}대")

            if '항공사' in df.columns:
                print(f"  - 항공사별 분포:")
                airline_counts = df['항공사'].value_counts()
                for airline, count in airline_counts.items():
                    if airline != 'Unknown':
                        print(f"    * {airline}: {count}대")

            # 고도별 분포
            if '고도' in df.columns:
                df_with_altitude = df[df['고도'].notna()]
                if not df_with_altitude.empty:
                    avg_altitude = df_with_altitude['고도'].mean()
                    max_altitude = df_with_altitude['고도'].max()
                    min_altitude = df_with_altitude['고도'].min()
                    print(f"  - 고도 정보:")
                    print(f"    * 평균 고도: {avg_altitude:,.0f}ft")
                    print(f"    * 최대 고도: {max_altitude:,.0f}ft")
                    print(f"    * 최소 고도: {min_altitude:,.0f}ft")

            # 상세 분석 실행
            analyze_aircraft_data(df)

            # 특정 기종 검색 예제
            print(f"\n🔍 특정 기종 검색 예제:")

            # Boeing 777 검색
            boeing_777 = get_aircraft_by_type(df, 'Boeing 777')
            if boeing_777 is not None and not boeing_777.empty:
                print(f"  - Boeing 777: {len(boeing_777)}대 발견")

            # Airbus A380 검색
            airbus_380 = get_aircraft_by_type(df, 'A380')
            if airbus_380 is not None and not airbus_380.empty:
                print(f"  - Airbus A380: {len(airbus_380)}대 발견")

            # 한국 항공사만 필터링
            korean_airlines = get_korean_airlines_only(df)
            if korean_airlines is not None and not korean_airlines.empty:
                print(f"\n🇰🇷 한국 항공사 항공기: {len(korean_airlines)}대")
                if '항공사' in korean_airlines.columns:
                    korean_counts = korean_airlines['항공사'].value_counts()
                    for airline, count in korean_counts.items():
                        print(f"  - {airline}: {count}대")

        else:
            print("❌ 데이터를 가져올 수 없습니다.")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

# 필요한 패키지 설치 명령어:
# pip install selenium pandas requests webdriver-manager

# 추가 기능:
# - 실제 항공기 데이터베이스 연동 (ICAO hex 코드 매핑)
# - 제조사별 통계 (Boeing vs Airbus 비교)
# - 한국 항공사 필터링
# - 고도/속도별 분석
# - 기종 식별 성공률 추적