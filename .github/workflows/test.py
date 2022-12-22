import os
import os.path as op


def red(message: str):
    print("\033[0;31m" + message + " 생성 실패\033[0m")


def green(message: str):
    print("\033[0;33m" + message + " 생성 완료\033[0m")


otl_home = os.environ.get('OTL_HOME')

if op.isdir(f'{otl_home}/module'):
    green("module 디렉토리")
    # 치환 모듈
    if op.isdir(f'{otl_home}/module/alteration'):
        green("alteration 디렉토리")
        if op.isfile(f'{otl_home}/module/alteration/origin.otlm'):
            green("alteration/origin.otlm 파일")
        else:
            red("alteration/origin.otlm 파일")
    else:
        red("alteration 디렉토리")
    # 강제 모듈
    if op.isdir(f'{otl_home}/module/compulsion'):
        green("compulsion 디렉토리")
        if op.isfile(f'{otl_home}/module/compulsion/origin.otlm'):
            green("compulsion/origin.otlm 파일")
        else:
            red("compulsion/origin.otlm 파일")
    else:
        red("compulsion 디렉토리")
    # 동작 모듈
    if op.isdir(f'{otl_home}/module/operate'):
        green("operate 디렉토리")
        if op.isfile(f'{otl_home}/module/operate/origin.otlm'):
            green("operate/origin.otlm 파일")
        else:
            red("operate/origin.otlm 파일")
    else:
        red("operate 디렉토리")

