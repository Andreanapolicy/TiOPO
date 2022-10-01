using Document.src.Command;
using Document.src.History;

namespace Document.src.Paragraph
{
    class CParagraph : IParagraph
    {
        public CParagraph(string text, ref IHistory history)
        {
            m_text = text;
            m_history = history;
        }

        public string GetText()
        {
            return m_text;
        }

        public void SetText(string text)
        {
            ICommand setTextCommand = new CReplaceTextParagraphCommand(ref m_text, ref text);
            m_history.AddAndExecuteCommand(ref setTextCommand);
        }

        private string m_text;
        private IHistory m_history;
    }
}
