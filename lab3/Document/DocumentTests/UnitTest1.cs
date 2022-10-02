using NUnit.Framework;
using Document.src.Document;
using DocumentTests.src.History;
using Document.src.History;

namespace DocumentTests
{
    public class DocumentTests
    {
        [Test]
        public void Check_Document_Constructing()
        {
            IHistory history = new CMockHistory();
            CDocument document = new CDocument(history);

            Assert.IsNotNull(document);
            Assert.AreEqual(document.GetTitle(), "");
            Assert.AreEqual(document.GetItemsCount(), 0);
            Assert.IsFalse(document.CanRedo());
            Assert.IsFalse(document.CanUndo());
        }

        [Test]
        public void Check_Document_Adding_Paragraph()
        {
        }
    }
}