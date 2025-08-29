#!/usr/bin/env python3
"""
Flight Data Adapter for Seoul Flight Tracker Integration
Integrates with seoul_flight.py to provide aircraft information for the chatbot.
"""

import logging
import pandas as pd
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import math
from datetime import datetime
import re

# Import the existing Seoul Flight Tracker
from seoul_flight import SeoulFlightTracker, analyze_aircraft_data

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class AircraftInfo:
    """Structured aircraft information."""
    callsign: str
    aircraft_type: str
    manufacturer: str
    model: str
    latitude: float
    longitude: float
    altitude: int
    heading: int
    speed: int
    airline: str
    registration: Optional[str] = None
    hex_code: Optional[str] = None
    last_updated: Optional[datetime] = None

@dataclass
class Airport:
    """Airport information."""
    code: str
    name: str
    latitude: float
    longitude: float
    elevation: int

class FlightDataAdapter:
    """Adapter for integrating seoul_flight.py with the aviation chatbot."""

    def __init__(self):
        self.flight_tracker = SeoulFlightTracker()
        self.cached_data = None
        self.last_update = None

        # Seoul area airports
        self.seoul_airports = {
            'RKSI': Airport('RKSI', 'Seoul Incheon International Airport', 37.4601, 126.4407, 23),
            'RKSS': Airport('RKSS', 'Seoul Gimpo International Airport', 37.5583, 126.7908, 18),
            'RKPC': Airport('RKPC', 'Jeju International Airport', 33.5070, 126.4963, 36),
            'RKPK': Airport('RKPK', 'Gimhae International Airport', 35.1795, 128.9382, 5),
            'RKTU': Airport('RKTU', 'Daegu International Airport', 35.8940, 128.6586, 79),
            'RKTN': Airport('RKTN', 'Cheongju International Airport', 36.7166, 127.4991, 191)
        }

        # Supported aircraft types for the chatbot
        self.supported_aircraft = {
            'Boeing 737', 'Boeing 747', 'Boeing 777',
            'Airbus A320', 'Airbus A321'
        }

    def is_supported_aircraft(self, aircraft_type: str) -> bool:
        """Check if aircraft type is supported by the chatbot."""
        return any(supported in aircraft_type for supported in self.supported_aircraft)

    def get_aircraft_by_callsign(self, callsign: str) -> Optional[AircraftInfo]:
        """
        Get aircraft information by callsign.

        Args:
            callsign: Aircraft callsign (e.g., 'KAL123', 'AAR456')

        Returns:
            AircraftInfo object or None if not found
        """
        try:
            # Get fresh flight data
            flight_data = self.flight_tracker.get_flight_data()

            if flight_data.empty:
                logger.error("No flight data available")
                return None

            # Convert to DataFrame for easier handling
            df = pd.DataFrame(flight_data)

            if df.empty:
                logger.error("Empty flight data received")
                return None

            # Search for the callsign (case insensitive)
            callsign_upper = callsign.upper().strip()

            # Try exact match first
            exact_match = df[df['편명'].str.upper() == callsign_upper]

            if not exact_match.empty:
                aircraft_row = exact_match.iloc[0]
            else:
                # Try partial match
                partial_match = df[df['편명'].str.upper().str.contains(callsign_upper, na=False)]
                if not partial_match.empty:
                    aircraft_row = partial_match.iloc[0]
                else:
                    logger.warning(f"Aircraft with callsign '{callsign}' not found")
                    return None

            # Get detailed aircraft type information
            aircraft_type_info = self.flight_tracker.get_aircraft_type_info(
                aircraft_row.get('type', ''),
                aircraft_row.get('hex', '')
            )

            # Get airline information
            airline = self.flight_tracker.get_airline_name(callsign)

            # Create AircraftInfo object
            aircraft_info = AircraftInfo(
                callsign=aircraft_row.get('편명', callsign),
                aircraft_type=f"{aircraft_row.get('제조사', 'Unknown')} {aircraft_row.get('기종', 'Unknown')}",
                manufacturer=aircraft_row.get('제조사', 'Unknown'),
                model=aircraft_row.get('기종명', aircraft_row.get('기종', 'Unknown')),
                latitude=float(aircraft_row.get('위도', 0)),
                longitude=float(aircraft_row.get('경도', 0)),
                altitude=int(aircraft_row.get('기압고도', 0)),
                heading=int(aircraft_row.get('방향', 0)),
                speed=int(aircraft_row.get('지상속도', 0)),
                airline=aircraft_row.get('항공사', 'Unknown'),
                registration=aircraft_row.get('reg', None),
                hex_code=aircraft_row.get('식별코드', None),
                last_updated=datetime.now()
            )

            logger.info(f"Found aircraft: {callsign} - {aircraft_info.aircraft_type}")
            return aircraft_info

        except Exception as e:
            logger.error(f"Error getting aircraft data for {callsign}: {str(e)}")
            return None

    def calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate distance between two points using Haversine formula.

        Returns:
            Distance in kilometers
        """
        # Convert degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))

        # Earth's radius in kilometers
        r = 6371

        return c * r

    def find_nearest_airports(self, aircraft: AircraftInfo, max_airports: int = 3) -> List[Tuple[Airport, float]]:
        """
        Find nearest airports to the aircraft.

        Args:
            aircraft: AircraftInfo object
            max_airports: Maximum number of airports to return

        Returns:
            List of (Airport, distance_km) tuples sorted by distance
        """
        airport_distances = []

        for airport in self.seoul_airports.values():
            distance = self.calculate_distance(
                aircraft.latitude, aircraft.longitude,
                airport.latitude, airport.longitude
            )
            airport_distances.append((airport, distance))

        # Sort by distance and return top results
        airport_distances.sort(key=lambda x: x[1])
        return airport_distances[:max_airports]

    def get_flight_status_summary(self, aircraft: AircraftInfo) -> Dict:
        """
        Get a comprehensive flight status summary.

        Args:
            aircraft: AircraftInfo object

        Returns:
            Dictionary with flight status information
        """
        nearest_airports = self.find_nearest_airports(aircraft, max_airports=3)

        return {
            'aircraft': {
                'callsign': aircraft.callsign,
                'type': aircraft.aircraft_type,
                'manufacturer': aircraft.manufacturer,
                'model': aircraft.model,
                'airline': aircraft.airline,
                'supported': self.is_supported_aircraft(aircraft.aircraft_type)
            },
            'position': {
                'latitude': aircraft.latitude,
                'longitude': aircraft.longitude,
                'altitude_ft': aircraft.altitude,
                'altitude_m': int(aircraft.altitude * 0.3048),
                'heading': aircraft.heading,
                'speed_kts': aircraft.speed,
                'speed_kmh': int(aircraft.speed * 1.852)
            },
            'nearest_airports': [
                {
                    'code': airport.code,
                    'name': airport.name,
                    'distance_km': round(distance, 1),
                    'distance_nm': round(distance * 0.539957, 1)
                }
                for airport, distance in nearest_airports
            ],
            'last_updated': aircraft.last_updated.isoformat() if aircraft.last_updated else None
        }

    def search_aircraft_by_type(self, aircraft_type: str, max_results: int = 10) -> List[AircraftInfo]:
        """
        Search for aircraft by type.

        Args:
            aircraft_type: Aircraft type to search for (e.g., 'Boeing 737')
            max_results: Maximum number of results to return

        Returns:
            List of AircraftInfo objects
        """
        try:
            flight_data = self.flight_tracker.get_flight_data()
            if not flight_data:
                return []

            df = pd.DataFrame(flight_data)
            results = []

            for _, row in df.iterrows():
                full_type = f"{row.get('제조사', 'Unknown')} {row.get('기종', 'Unknown')}"

                if aircraft_type.lower() in full_type.lower():
                    aircraft_info = AircraftInfo(
                        callsign=row.get('편명', ''),
                        aircraft_type=full_type,
                        manufacturer=row.get('제조사', 'Unknown'),
                        model=row.get('기종명', row.get('기종', 'Unknown')),
                        latitude=float(row.get('위도', 0)),
                        longitude=float(row.get('경도', 0)),
                        altitude=int(row.get('기압고도', 0)),
                        heading=int(row.get('방향', 0)),
                        speed=int(row.get('지상속도', 0)),
                        airline=row.get('항공사', 'Unknown'),
                        registration=row.get('reg', None),
                        hex_code=row.get('식별코드', None),
                        last_updated=datetime.now()
                    )

                    results.append(aircraft_info)

                    if len(results) >= max_results:
                        break

            return results

        except Exception as e:
            logger.error(f"Error searching aircraft by type {aircraft_type}: {str(e)}")
            return []

    def get_airport_info(self, airport_code: str) -> Optional[Airport]:
        """Get airport information by ICAO code."""
        return self.seoul_airports.get(airport_code.upper())

    def get_all_airports(self) -> List[Airport]:
        """Get all supported airports."""
        return list(self.seoul_airports.values())


def main():
    """Test the flight data adapter."""
    adapter = FlightDataAdapter()

    print("="*60)
    print("FLIGHT DATA ADAPTER TEST")
    print("="*60)

    # Test getting current flight data
    try:
        flight_data = adapter.flight_tracker.get_flight_data()
        if flight_data:
            df = pd.DataFrame(flight_data)
            print(f"✅ Found {len(df)} active flights around Seoul")

            # Show some sample callsigns
            sample_callsigns = df['편명'].head(5).tolist()
            print(f"Sample callsigns: {sample_callsigns}")

            # Test aircraft lookup
            if sample_callsigns:
                test_callsign = sample_callsigns[0]
                print(f"\n🔍 Testing aircraft lookup for: {test_callsign}")

                aircraft = adapter.get_aircraft_by_callsign(test_callsign)
                if aircraft:
                    print(f"✅ Aircraft found: {aircraft.aircraft_type}")
                    print(f"   Position: {aircraft.latitude:.4f}, {aircraft.longitude:.4f}")
                    print(f"   Altitude: {aircraft.altitude} ft")
                    print(f"   Airline: {aircraft.airline}")
                    print(f"   Supported: {adapter.is_supported_aircraft(aircraft.aircraft_type)}")

                    # Test nearest airports
                    nearest = adapter.find_nearest_airports(aircraft)
                    print(f"   Nearest airports:")
                    for airport, distance in nearest:
                        print(f"     - {airport.code} ({airport.name}): {distance:.1f} km")

        else:
            print("❌ No flight data available")

    except Exception as e:
        print(f"❌ Error testing adapter: {str(e)}")

    # Test airport information
    print(f"\n🏢 Available airports:")
    for airport in adapter.get_all_airports():
        print(f"   - {airport.code}: {airport.name}")


if __name__ == "__main__":
    main()