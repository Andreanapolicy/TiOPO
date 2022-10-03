using System.Text;

namespace Document.src.Command
{
    public class CReplaceTextParagraphCommand : ICommand
    {
        public CReplaceTextParagraphCommand(StringBuilder currentText, StringBuilder newText)
        {
            m_currentText = currentText;
            m_newText = newText;
        }

        public void Execute()
        {
            StringBuilder temp = new StringBuilder(m_currentText.ToString());
            m_currentText.Clear();
            m_currentText.Append(m_newText.ToString());
            m_newText.Clear();
            m_newText.Append(temp.ToString());
        }

        public void Unexecute()
        {
            StringBuilder temp = new StringBuilder(m_currentText.ToString());
            m_currentText.Clear();
            m_currentText.Append(m_newText.ToString());
            m_newText.Clear();
            m_newText.Append(temp.ToString());
        }

        private StringBuilder m_currentText;
        private StringBuilder m_newText;
    }
}
