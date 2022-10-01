namespace Document.src.Command
{
    class CReplaceTextParagraphCommand : ICommand
    {
        public CReplaceTextParagraphCommand(ref string currentText, ref string newText)
        {
            m_currentText = currentText;
            m_newText = newText;
        }

        public void Execute()
        {
            (m_currentText, m_newText) = (m_newText, m_currentText);
        }

        public void Unexecute()
        {
            (m_currentText, m_newText) = (m_newText, m_currentText);
        }

        private string m_currentText;
        private string m_newText;
    }
}
