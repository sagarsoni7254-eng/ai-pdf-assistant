from llama_index.core.node_parser import SentenceSplitter

splitter = SentenceSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)


def split_text(text: str) -> list[str]:
    """
    Split large text into overlapping chunks.
    """

    return splitter.split_text(text)