#!/usr/bin/env python3
"""
LangGraph Workflow Visualization Generator
워크플로우 그래프 이미지를 생성하는 독립 스크립트
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app_gradio import AviationLangGraphSystem

def main():
    """Generate workflow visualization."""
    print("🔧 LangGraph 워크플로우 시각화 생성 중...")
    
    try:
        # Create aviation system (without launching Gradio)
        aviation_system = AviationLangGraphSystem()
        print("✅ 시스템 초기화 완료")
        
        # Generate workflow visualization
        image_path = aviation_system.visualize_workflow("langgraph_aviation_workflow.png")
        
        if image_path and os.path.exists(image_path):
            print(f"📊 워크플로우 그래프 생성 완료: {image_path}")
            print(f"📁 파일 크기: {os.path.getsize(image_path):,} bytes")
            
            # Also create a simplified version
            simple_path = aviation_system.visualize_workflow("workflow_simple.png")
            if simple_path and os.path.exists(simple_path):
                print(f"📊 간단 버전도 생성: {simple_path}")
            
        else:
            print("❌ 워크플로우 그래프 생성 실패")
            
    except Exception as e:
        print(f"❌ 오류 발생: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()