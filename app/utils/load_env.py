import os
from dotenv import load_dotenv


def load_environment_variables(env_file='.env'):
    """
    .env 파일을 불러와 환경 변수를 설정하는 함수

    Parameters:
    env_file (str): 사용할 .env 파일의 경로 (기본값: '.env')

    Returns:
    bool: 파일이 성공적으로 로드되면 True, 그렇지 않으면 False
    """
    try:
        # .env 파일 로드
        load_dotenv(env_file)

        # 성공적으로 파일이 로드되었는지 확인
        if os.path.exists(env_file):
            print(f'{env_file} 파일에서 환경 변수를 성공적으로 불러왔습니다.')
            return True
        else:
            print(f'{env_file} 파일을 찾을 수 없습니다.')
            return False
    except Exception as e:
        print(f'환경 변수를 불러오는 중 오류가 발생했습니다: {e}')
        return False

