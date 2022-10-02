using Document.src.Paragraph;

namespace Document.src.DocumentItem
{
    public interface IDocumentItem
    {
        IParagraph GetItem();
    }
}
