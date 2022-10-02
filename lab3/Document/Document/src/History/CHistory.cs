using Document.src.Command;

namespace Document.src.History
{
    public class CHistory : IHistory
    {
        public bool CanRedo()
        {
            // log some information
            return m_next > 0;
        }

        public bool CanUndo()
        {
            // log some information
            return m_next < m_commands.Count;
        }

        public void Redo()
        {
            if (CanRedo())
            {
                m_commands[--m_next].Unexecute();
            }
            // log some information
        }

        public void Undo()
        {
            if (CanUndo())
            {
                m_commands[++m_next].Execute();
            }
            // log some information
        }

        public void AddAndExecuteCommand(ref ICommand command)
        {
            command.Execute();

            for(int index = m_next; index < m_commands.Count; index++)
            {
                m_commands.RemoveAt(index);
            }

            m_commands.Add(command);
            m_next++;

            if (m_next == HISTORY_LIMIT + 1)
            {
                m_commands.RemoveAt(0);
                m_next--;
            }

            // log some information
        }

        private const int HISTORY_LIMIT = 10;
        private int m_next = 0;
        private List<ICommand> m_commands = new List<ICommand>();
    }
}
