def main():
    # 세미나와 교실 매핑
    seminar_to_class = {
        "Algorithm": 204,
        "DataAnalysis": 207,
        "ArtificialIntelligence": 302,
        "CyberSecurity": "B101",
        "Network": 303,
        "Startup": 501,
        "TestStrategy": 105
    }
    
    # 입력 받기
    N = int(input())
    seminars = [input().strip() for _ in range(N)]
    
    # 출력
    for seminar in seminars:
        print(seminar_to_class[seminar])

if __name__ == "__main__":
    main()
