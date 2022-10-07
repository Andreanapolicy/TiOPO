using NUnit.Framework;
using Document.src.Document;
using DocumentTests.src.History;
using Document.src.History;

namespace DocumentTests
{
    public class DocumentTests
    {
        private IHistory m_history;

        private void checkHistoryState(ref IDocument document, bool isAvailableUndo, bool isAvailableRedo)
        {
            Assert.AreEqual(document.CanRedo(), isAvailableRedo);
            Assert.AreEqual(document.CanUndo(), isAvailableUndo);
        }

        [SetUp]
        public void CreateHistory()
        {
            this.m_history = new CMockHistory();
        }

        [Test]
        public void Check_Document_Constructing()
        {
            IDocument document = new CDocument(m_history);

            Assert.IsNotNull(document);
            Assert.AreEqual(document.GetTitle(), "");
            Assert.AreEqual(document.GetItemsCount(), 0);
            checkHistoryState(ref document, false, false);
        }

        [Test]
        public void Check_Document_Setting_Title_With_Value()
        {
            IDocument document = new CDocument(m_history);

            document.SetTitle("Title");

            Assert.AreEqual(document.GetTitle(), "Title");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Setting_Title_With_Empty_Value()
        {
            IDocument document = new CDocument(m_history);

            document.SetTitle("");

            Assert.AreEqual(document.GetTitle(), "");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Adding_Paragraph_Into_Wrong_Position()
        {
            IDocument document = new CDocument(m_history);

            Assert.Catch(() => document.InsertParagraph("test", 1), "Index is out of range");

            Assert.AreEqual(document.GetItemsCount(), 0);
            checkHistoryState(ref document, false, false);
        }

        [Test]
        public void Check_Document_Adding_Paragraph_Into_Right_Position()
        {
            IDocument document = new CDocument(m_history);

            document.InsertParagraph("test", 0);

            Assert.AreEqual(document.GetItemsCount(), 1);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "test");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Adding_Paragraphs()
        {
            IDocument document = new CDocument(m_history);

            document.InsertParagraph("test", 0);
            document.InsertParagraph("test1", 1);
            document.InsertParagraph("test2", 2);

            Assert.AreEqual(document.GetItemsCount(), 3);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "test");
            Assert.AreEqual(document.GetItem(1).GetItem().GetText(), "test1");
            Assert.AreEqual(document.GetItem(2).GetItem().GetText(), "test2");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Getting_Wrong_Element()
        {
            IDocument document = new CDocument(m_history);

            Assert.Catch(() => document.GetItem(1), "Index is out of range");

            Assert.AreEqual(document.GetItemsCount(), 0);
            checkHistoryState(ref document, false, false);
        }

        [Test]
        public void Check_Document_Removing_Alone_Paragraph()
        {
            IDocument document = new CDocument(m_history);
            document.InsertParagraph("test", 0);
            
            document.RemoveItem(0);
            
            Assert.AreEqual(document.GetItemsCount(), 0);
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Removing_First_Paragraph()
        {
            IDocument document = new CDocument(m_history);
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
            IDocument document = new CDocument(m_history);
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
            IDocument document = new CDocument(m_history);
            document.InsertParagraph("1", 0);
            document.InsertParagraph("2", 1);
            document.InsertParagraph("3", 2);

            document.RemoveItem(2);
            
            Assert.AreEqual(document.GetItemsCount(), 2);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "1");
            Assert.AreEqual(document.GetItem(1).GetItem().GetText(), "2");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Removing_Wrong_Paragraph()
        {
            IDocument document = new CDocument(m_history);
            
            Assert.Catch(() => document.RemoveItem(2), "Index is out of range");

            Assert.AreEqual(document.GetItemsCount(), 0);
            checkHistoryState(ref document, false, false);
        }

        [Test]
        public void Check_Document_Replacing_Paragraph_Text_Success()
        {
            IDocument document = new CDocument(m_history);
            document.InsertParagraph("1", 0);

            document.ReplaceParagraphText(0, "2");

            Assert.AreEqual(document.GetItemsCount(), 1);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "2");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Replacing_Paragraph_On_Empty_Value()
        {
            IDocument document = new CDocument(m_history);
            document.InsertParagraph("1", 0);

            document.ReplaceParagraphText(0, "");

            Assert.AreEqual(document.GetItemsCount(), 1);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Replacing_Paragraph_Text_Wrong_Position()
        {
            IDocument document = new CDocument(m_history);

            Assert.Catch(() => document.ReplaceParagraphText(0, "2"), "Index is out of range");

            Assert.AreEqual(document.GetItemsCount(), 0);
            checkHistoryState(ref document, false, false);
        }

        [Test]
        public void Check_Document_Replacing_First_Paragraph_With_2_Additional_Paragraph()
        {
            IDocument document = new CDocument(m_history);
            document.InsertParagraph("0", 0);
            document.InsertParagraph("1", 1);
            document.InsertParagraph("2", 2);

            document.ReplaceParagraphText(0, "test");

            Assert.AreEqual(document.GetItemsCount(), 3);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "test");
            Assert.AreEqual(document.GetItem(1).GetItem().GetText(), "1");
            Assert.AreEqual(document.GetItem(2).GetItem().GetText(), "2");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Replacing_Second_Paragraph_With_2_Additional_Paragraph()
        {
            IDocument document = new CDocument(m_history);
            document.InsertParagraph("0", 0);
            document.InsertParagraph("1", 1);
            document.InsertParagraph("2", 2);

            document.ReplaceParagraphText(1, "test");

            Assert.AreEqual(document.GetItemsCount(), 3);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "0");
            Assert.AreEqual(document.GetItem(1).GetItem().GetText(), "test");
            Assert.AreEqual(document.GetItem(2).GetItem().GetText(), "2");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Replacing_Third_Paragraph_With_2_Additional_Paragraph()
        {
            IDocument document = new CDocument(m_history);
            document.InsertParagraph("0", 0);
            document.InsertParagraph("1", 1);
            document.InsertParagraph("2", 2);

            document.ReplaceParagraphText(2, "test");

            Assert.AreEqual(document.GetItemsCount(), 3);
            Assert.AreEqual(document.GetItem(0).GetItem().GetText(), "0");
            Assert.AreEqual(document.GetItem(1).GetItem().GetText(), "1");
            Assert.AreEqual(document.GetItem(2).GetItem().GetText(), "test");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Undo_With_One_Command()
        {
            IDocument document = new CDocument(m_history);
            document.SetTitle("1");

            document.Undo();

            Assert.AreEqual(document.GetTitle(), "");
            checkHistoryState(ref document, false, true);
        }

        [Test]
        public void Check_Document_Undo_With_Many_Command()
        {
            IDocument document = new CDocument(m_history);
            document.SetTitle("1");
            document.SetTitle("2");

            document.Undo();

            Assert.AreEqual(document.GetTitle(), "1");
            checkHistoryState(ref document, true, true);
        }

        [Test]
        public void Check_Document_Redo_With_One_Command()
        {
            IDocument document = new CDocument(m_history);
            document.SetTitle("1");
            document.Undo();

            document.Redo();

            Assert.AreEqual(document.GetTitle(), "1");
            checkHistoryState(ref document, true, false);
        }

        [Test]
        public void Check_Document_Redo_With_Many_Command()
        {
            IDocument document = new CDocument(m_history);
            document.SetTitle("1");
            document.SetTitle("2");
            document.Undo();

            document.Redo();

            Assert.AreEqual(document.GetTitle(), "2");
            checkHistoryState(ref document, true, false);
        }
    }
}