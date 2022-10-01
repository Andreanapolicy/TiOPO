namespace Document.src.Command
{
    interface ICommand
    {
        void Execute();

        void Unexecute();

    }
}
