using Document.src.DocumentItem;
using Document.src.Paragraph;

namespace Document.src.Document
{
    interface IDocument
    {
		IParagraph InsertParagraph(string text, int position);

		IDocumentItem GetItem(int index);

		void SetTitle(string title);

		string GetTitle();

		int GetItemsCount();

		void ReplaceParagraphText(int index, string text);

		void RemoveItem(int index);

		bool CanUndo();
		
		void Undo();

		bool CanRedo();
		
		void Redo();
    }
}
