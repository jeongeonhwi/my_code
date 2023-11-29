# 2등분 내는 코드
def split_text(input_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # 텍스트의 중간 지점을 찾아서 나눕니다.
    middle = len(content) // 2

    # 나뉜 텍스트를 파일로 저장합니다.
    chunk1 = content[:middle]
    chunk2 = content[middle:]

    with open("output_chunk_1.txt", 'w') as file:
        file.write(chunk1)
        print("Chunk 1 saved to output_chunk_1.txt")

    with open("output_chunk_2.txt", 'w') as file:
        file.write(chunk2)
        print("Chunk 2 saved to output_chunk_2.txt")

if __name__ == "__main__":
    # 텍스트 파일 경로를 설정합니다.
    input_file_path = "input.txt"  # 원본 텍스트 파일 경로

    split_text(input_file_path)
