namespace Document.src.Command
{
    class CChangeTitleCommand : ICommand
    {
        public CChangeTitleCommand(ref string currentTitle, ref string newTitle)
        {
            m_currentTitle = currentTitle;
            m_newTitle = newTitle;
        }

        public void Execute()
        {
            (m_currentTitle, m_newTitle) = (m_newTitle, m_currentTitle);
        }

        public void Unexecute()
        {
            (m_currentTitle, m_newTitle) = (m_newTitle, m_currentTitle);
        }

        private string m_currentTitle;
        private string m_newTitle;
    }
}
