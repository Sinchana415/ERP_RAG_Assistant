from src.rag import get_qa_chain

def test_erp_query():
    qa = get_qa_chain()
    result = qa("What is the vendor payment policy?")
    assert len(result["result"]) > 0
