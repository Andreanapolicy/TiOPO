using Document.src.Command;

namespace Document.src.History
{
    public interface IHistory
    {
        bool CanUndo();
        
        bool CanRedo();
        
        void Undo();

        void Redo();

        void AddAndExecuteCommand(ref ICommand command);
    }
}
