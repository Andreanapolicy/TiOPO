using Document.src.Command;
using Document.src.DocumentItem;
using Document.src.History;
using Document.src.Paragraph;
using System.Text;

namespace Document.src.Document
{
    public class CDocument : IDocument
    {
        public CDocument(IHistory history)
        {
            m_history = history;
        }

        public IDocumentItem GetItem(int index)
        {
            return m_items.ElementAt(index);
        }

        public int GetItemsCount()
        {
            return m_items.Count;
        }

        public string GetTitle()
        {
            return m_title.ToString();
        }

        public IParagraph InsertParagraph(string text, int position)
        {
            IParagraph paragraph = new CParagraph(text, ref m_history);
            IDocumentItem newDocumentItem = new CDocumentItem(paragraph);
            ICommand insertParagraphCommand = new CInsertDocumentItemCommand(ref m_items, ref newDocumentItem, position);

            m_history.AddAndExecuteCommand(ref insertParagraphCommand);

            return paragraph;
        }

        public void RemoveItem(int index)
        {
            ICommand removeItemCommand = new CRemoveItemCommand(ref m_items, index);
            m_history.AddAndExecuteCommand(ref removeItemCommand);
        }

        public void ReplaceParagraphText(int index, string text)
        {
            if (index > m_items.Count)
            {
                throw new ArgumentOutOfRangeException("Index is out of range");
            }

            IDocumentItem item = m_items[index];
            item.GetItem().SetText(text);
        }

        public void SetTitle(string title)
        {
            StringBuilder titleSB = new StringBuilder(title);
            ICommand setTitleCommand = new CChangeTitleCommand(m_title, titleSB);
            m_history.AddAndExecuteCommand(ref setTitleCommand);
        }

        public bool CanRedo()
        {
            return m_history.CanRedo();
        }

        public bool CanUndo()
        {
            return m_history.CanUndo();
        }

        public void Undo()
        {
            m_history.Undo();
        }

        public void Redo()
        {
            m_history.Redo();
        }

        private IHistory m_history;
        private StringBuilder m_title = new StringBuilder("");
        private List<IDocumentItem> m_items = new List<IDocumentItem>();
    }
}
