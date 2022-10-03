using Document.src.Command;
using Document.src.History;
using System.Text;

namespace Document.src.Paragraph
{
    public class CParagraph : IParagraph
    {
        public CParagraph(string text, ref IHistory history)
        {
            m_text = new StringBuilder(text);
            m_history = history;
        }

        public string GetText()
        {
            return m_text.ToString();
        }

        public void SetText(string text)
        {
            StringBuilder textSB = new StringBuilder(text);
            ICommand setTextCommand = new CReplaceTextParagraphCommand(m_text, textSB);
            m_history.AddAndExecuteCommand(ref setTextCommand);
        }

        private StringBuilder m_text;
        private IHistory m_history;
    }
}
