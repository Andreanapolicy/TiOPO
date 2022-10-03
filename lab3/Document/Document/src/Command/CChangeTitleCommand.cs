using System.Text;

namespace Document.src.Command
{
    public class CChangeTitleCommand : ICommand
    {
        public CChangeTitleCommand(StringBuilder currentTitle, StringBuilder newTitle)
        {
            m_currentTitle = currentTitle;
            m_newTitle = newTitle;
        }

        public void Execute()
        {
            StringBuilder temp = new StringBuilder(m_currentTitle.ToString());
            m_currentTitle.Clear();
            m_currentTitle.Append(m_newTitle.ToString());
            m_newTitle.Clear();
            m_newTitle.Append(temp.ToString());

        }

        public void Unexecute()
        {
            StringBuilder temp = new StringBuilder(m_currentTitle.ToString());
            m_currentTitle.Clear();
            m_currentTitle.Append(m_newTitle.ToString());
            m_newTitle.Clear();
            m_newTitle.Append(temp.ToString());
        }

        private StringBuilder m_currentTitle;
        private StringBuilder m_newTitle;
    }
}
