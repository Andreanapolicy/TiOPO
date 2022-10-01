namespace Document.src.Paragraph
{
    class CParagraph : IParagraph
    {
        CParagraph(string text, IHistory history)
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
            m_history.AddAndExecuteCommand(new CReplaceTextParagraphCommand(m_text, text));
        }

        private string m_text;
        private IHistory m_history;
    }
}
