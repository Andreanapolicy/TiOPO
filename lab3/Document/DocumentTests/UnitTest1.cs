using NUnit.Framework;
using Document.src.Document;
using DocumentTests.src.History;
using Document.src.History;

namespace DocumentTests
{
    public class DocumentTests
    {
        [Test]
        public void CreateDocument()
        {
            IHistory history = new CMockHistory();
            CDocument document = new CDocument(history);
        }
    }
}