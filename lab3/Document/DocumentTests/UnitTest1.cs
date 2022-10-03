using NUnit.Framework;
using Document.src.Document;
using DocumentTests.src.History;
using Document.src.History;

namespace DocumentTests
{
    public class DocumentTests
    {
        public void checkHistoryState(ref IDocument document, bool isAvailableUndo, bool isAvailableRedo)
        {
            Assert.AreEqual(document.CanRedo(), isAvailableRedo);
            Assert.AreEqual(document.CanUndo(), isAvailableUndo);
        }

        [Test]
        public void Check_Document_Constructing()
        {
            IHistory history = new CMockHistory();
            IDocument document = new CDocument(history);

            Assert.IsNotNull(document);
            Assert.AreEqual(document.GetTitle(), "");
            Assert.AreEqual(document.GetItemsCount(), 0);
            checkHistoryState(ref document, false, false);
        }

        [Test]
        public void Check_Document_Setting_Title()
        {
            IHistory history = new CMockHistory();
            IDocument document = new CDocument(history);

            document.SetTitle("Title");

            Assert.AreEqual(document.GetTitle(), "Title");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Adding_Paragraph_Into_Wrong_Position()
        {
            IHistory history = new CMockHistory();
            CDocument document = new CDocument(history);

            Assert.Catch(() => document.InsertParagraph("test", 1), "Index is out of range");
        }

        [Test]
        public void Check_Document_Adding_Paragraph_Into_Right_Position()
        {
            IHistory history = new CMockHistory();
            IDocument document = new CDocument(history);

            Assert.DoesNotThrow(() => document.InsertParagraph("test", 0));

            Assert.AreEqual(document.GetItemsCount(), 1);
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Removing_Alone_Paragraph()
        {
            IHistory history = new CMockHistory();
            IDocument document = new CDocument(history);
            document.InsertParagraph("test", 0);
            document.RemoveItem(0);
            
            Assert.AreEqual(document.GetItemsCount(), 0);
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Removing_First_Paragraph()
        {
            IHistory history = new CMockHistory();
            IDocument document = new CDocument(history);
            document.InsertParagraph("1", 0);
            document.InsertParagraph("2", 1);
            document.InsertParagraph("3", 2);
            document.RemoveItem(0);
            
            Assert.AreEqual(document.GetItemsCount(), 2);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "2");
            Assert.AreEqual(document.GetItem(1).GetItem().GetText(), "3");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Removing_Second_Paragraph()
        {
            IHistory history = new CMockHistory();
            IDocument document = new CDocument(history);
            document.InsertParagraph("1", 0);
            document.InsertParagraph("2", 1);
            document.InsertParagraph("3", 2);
            document.RemoveItem(1);
            
            Assert.AreEqual(document.GetItemsCount(), 2);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "1");
            Assert.AreEqual(document.GetItem(1).GetItem().GetText(), "3");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Removing_Third_Paragraph()
        {
            IHistory history = new CMockHistory();
            IDocument document = new CDocument(history);
            document.InsertParagraph("1", 0);
            document.InsertParagraph("2", 1);
            document.InsertParagraph("3", 2);
            document.RemoveItem(2);
            
            Assert.AreEqual(document.GetItemsCount(), 2);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "1");
            Assert.AreEqual(document.GetItem(1).GetItem().GetText(), "2");
            checkHistoryState(ref document, true, false);
        }
    }
}