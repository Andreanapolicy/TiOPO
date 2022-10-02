namespace Document.src.Command
{
    public interface ICommand
    {
        void Execute();

        void Unexecute();

    }
}
