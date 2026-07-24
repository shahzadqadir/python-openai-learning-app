from base_classes.indexer import DocIndexer

def main():
    indexer = DocIndexer(
        llm_model="buddy",
        embed_model="nomic-embed-text",
        data_folder="data",
        persist_directory="storage",
        base_url="http://host.docker.internal:11434"
    )
    indexer.set_query_engine()
    while True:
        question = input("Ask (type bye to quit)> ")
        if "bye" not in question.lower():
            answer = indexer.ask(question)
            print(answer)
        else:
            break

if __name__ == "__main__":
    main()