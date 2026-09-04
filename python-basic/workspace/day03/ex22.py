# 파일 쓰기
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요.\n")  # 개행 X, -> 이스케이프 문자로 개행
    f.write("점심을 먹었더니 졸리네요.\n")
    f.writelines(["hello\t", "python"])  # 개행 X
    print("hahaha", file=f)  # 자동 개행


# 파일 이어서 쓰기 : "오늘은 금요일, 내일은 주말"
with open("a.txt", "a", encoding="utf-8") as f:
    f.write("오늘은 금요일, 내일은 주말!\n")
