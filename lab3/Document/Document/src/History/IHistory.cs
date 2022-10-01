namespace Document.src.History
{
    interface IHistory
    {
        bool CanUndo();
        
        bool CanRedo();
        
        void Undo();

        void Redo();

        void AddAndExecuteCommand(ICommand command);
    }
}
