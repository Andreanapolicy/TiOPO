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

		void ResizeImage(int index, int width, int height);

		void ReplaceParagraphText(int index, string text);

		void RemoveItem(int index);

		void Save(string path);

		bool CanUndo();
		
		void Undo();

		bool CanRedo();
		
		void Redo();
    }
}
