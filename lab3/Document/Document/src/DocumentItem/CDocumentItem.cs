using Document.src.Paragraph;

namespace Document.src.DocumentItem
{
    public class CDocumentItem : IDocumentItem
    {
        public CDocumentItem(IParagraph item)
        {
            m_item = item;
        }

        public IParagraph GetItem()
        {
            return m_item;
        }

        private IParagraph m_item;
    }
}
