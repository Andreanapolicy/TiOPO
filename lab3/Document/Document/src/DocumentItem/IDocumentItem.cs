using Document.src.Paragraph;

namespace Document.src.DocumentItem
{
    interface IDocumentItem
    {
        IParagraph GetItem();
    }
}
