public class Main
{
    public static void main(String args[])
    {
        char[][] board;

    public Main()
        {
            board = new char[3][3];
        }

        void initBoard ()
        {
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j <= board[1].length; j++) {
                    board[i][j] = '';
                }
            }
        }

        void dispBoard
        {
            System.out.println("---------------------");
            for (int i = 0; i < board.length; i++)
            {
                System.out.print("|");
                for (int j = 0; j <= board[1].length; j++)
                {
                    System.out.print(board[i][j] + "|");
                    board[i][j] = '';
                }
                System.out.println(" ");
            }
        }

    }

}
