using Document.src.DocumentItem;

namespace Document.src.Command
{
    class CRemoveItemCommand : ICommand
    {
        public CRemoveItemCommand(ref List<IDocumentItem> items, int index)
        {
            m_items = items;
            m_index = index;

            if (m_index >= m_items.Count)
            {
                throw new ArgumentException("Index is out of range");
            }

            m_item = m_items[m_index];
        }

        public void Execute()
        {
            m_items.RemoveAt(m_index);
        }

        public void Unexecute()
        {
            m_items.Insert(m_index, m_item);
        }

        private List<IDocumentItem> m_items;
        private IDocumentItem m_item;
        private int m_index;
    }
}
