using Document.src.Command;

namespace Document.src.History
{
    interface IHistory
    {
        bool CanUndo();
        
        bool CanRedo();
        
        void Undo();

        void Redo();

        void AddAndExecuteCommand(ref ICommand command);
    }
}
