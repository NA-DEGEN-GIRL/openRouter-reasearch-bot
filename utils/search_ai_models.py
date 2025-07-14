import sys
import requests
import os

API_URL = "https://openrouter.ai/api/v1/models"
OUTFILE = "model_search_result.txt"

def fetch_models():
    try:
        resp = requests.get(API_URL)
        resp.raise_for_status()
        return resp.json().get("data", [])
    except Exception as e:
        print(f"모델 정보 불러오기 실패: {e}")
        sys.exit(1)

def print_model_info(model):
    print("="*70)
    print(f"모델 ID        : {model.get('id', '-')}")
    print(f"이름           : {model.get('name', '-')}")
    print(f"설명           : {model.get('description', '-')}")
    print(f"최대 컨텍스트  : {model.get('context_length', '-')}")
    print(f"지원입력       : {model.get('architecture',{}).get('input_modalities','-')}")
    print(f"지원출력       : {model.get('architecture',{}).get('output_modalities','-')}")
    print(f"지원 파라미터  : {', '.join(model.get('supported_parameters', []))}")
    print("")

def save_results(models, outfile=OUTFILE):
    with open(outfile, "w", encoding="utf-8") as f:
        for model in models:
            f.write("="*70 + "\n")
            f.write(f"모델 ID        : {model.get('id', '-')}\n")
            f.write(f"이름           : {model.get('name', '-')}\n")
            f.write(f"설명           : {model.get('description', '-')}\n")
            f.write(f"최대 컨텍스트  : {model.get('context_length', '-')}\n")
            f.write(f"지원입력       : {model.get('architecture',{}).get('input_modalities','-')}\n")
            f.write(f"지원출력       : {model.get('architecture',{}).get('output_modalities','-')}\n")
            f.write(f"지원 파라미터  : {', '.join(model.get('supported_parameters', []))}\n")
            f.write("\n")
    print(f"\n검색 결과가 '{outfile}'에 저장되었습니다.")

def main():
    # 커맨드라인 인자가 있을 경우: 그걸로 검색
    keyword = " ".join(sys.argv[1:]).strip().lower()
    models = fetch_models()

    if not models:
        print("가져온 모델 정보가 없습니다.")
        sys.exit(1)

    if not keyword:
        print(f"전체 {len(models)}개의 모델을 보여줍니다.\n")
        matches = models
    else:
        matches = []
        for m in models:
            text = "|".join([
                m.get('id',''), m.get('name',''), m.get('description',''), m.get('canonical_slug','')
            ]).lower()
            if keyword in text:
                matches.append(m)
        if not matches:
            print(f"'{keyword}'에 해당하는 모델이 없습니다.")
            return
        print(f"총 {len(matches)}개의 결과가 있습니다.\n")
    for m in matches:
        print_model_info(m)
    save_results(matches)

if __name__ == "__main__":
    main()
