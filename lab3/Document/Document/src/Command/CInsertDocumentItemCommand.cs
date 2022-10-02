using Document.src.DocumentItem;

namespace Document.src.Command
{
    public class CInsertDocumentItemCommand : ICommand
    {
        public CInsertDocumentItemCommand(ref List<IDocumentItem> items, ref IDocumentItem newItem, int index)
        {
            m_items = items;
            m_newItem = newItem;
            m_index = index;

            if (index > items.Count)
            {
                throw new ArgumentException("Index is out of range");
            }
        }

        public void Execute()
        {
            m_items.Insert(m_index, m_newItem);
        }

        public void Unexecute()
        {
            m_items.RemoveAt(m_index);
        }

        private List<IDocumentItem> m_items;
        private IDocumentItem m_newItem;
        private int m_index;
    }
}
