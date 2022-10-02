using Document.src.Command;
using System.Collections.Generic;

namespace DocumentTests.src.History
{
    public class CMockHistory
    {
        public bool CanRedo()
        {
            return m_next > 0;
        }

        public bool CanUndo()
        {
            return m_next < m_commands.Count;
        }

        public void Redo()
        {
            if (CanRedo())
            {
                m_commands[--m_next].Unexecute();
            }
        }

        public void Undo()
        {
            if (CanUndo())
            {
                m_commands[++m_next].Execute();
            }
        }

        public void AddAndExecuteCommand(ref ICommand command)
        {
            command.Execute();

            for (int index = m_next; index < m_commands.Count; index++)
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
        }

        private const int HISTORY_LIMIT = 10;
        private int m_next = 0;
        private List<ICommand> m_commands = new List<ICommand>();
    }
}
