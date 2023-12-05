def split_text(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 나뉜 텍스트를 파일로 저장합니다.
    total_chunks = 10
    chunk_size = len(content) // total_chunks

    for i in range(total_chunks):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < total_chunks - 1 else None

        # 나뉜 텍스트를 파일로 저장합니다.
        chunk = content[start:end]
        output_file_path = f"output_chunk_{i + 1}.txt"

        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(chunk)
            print(f"Chunk {i + 1} saved to {output_file_path}")

if __name__ == "__main__":
    # 텍스트 파일 경로를 설정합니다.
    input_file_path = "input.txt"  # 원본 텍스트 파일 경로

    split_text(input_file_path)
