import board.Board;
import board.Icon;

import java.util.Arrays;
import java.util.Scanner;

public class Game {

    /**
     * Which Player is currently active
     */
    private Icon player;
    /**
     * The board for this game
     */
    private Board board;

    /**
     * Creates a new game.
     * The player is set to 'X'.
     * The board is created.
     */
    public Game() {
        this.player = Icon.X;
        this.board = new Board();
    }

    public static void main(String[] args) {
        Game game = new Game();
        boolean flag;
        Board board = game.getBoard();
        while (!game.isGameOver()) {
            System.out.println(board.drawBoard());
            System.out.println("=".repeat(10));
            System.out.println(Board.drawGuide());
            do {
                flag = false;
                try {
                    board.update(game.getPlayer(), game.readInput());
                } catch (IndexOutOfBoundsException e) {
                    flag = true;
                } catch (IllegalArgumentException e) {
                    System.out.println("That location is already full");
                    flag = true;
                }
            } while (flag);
            game.flipPlayer();
        }
        game.flipPlayer();
        System.out.println("Congrats " + game.getPlayer() + " won.");
    }

    /**
     * Gets the current player.
     *
     * @return the current player
     */
    public Icon getPlayer() {
        return player;
    }

    /**
     * Sets the current player.
     * If player is X, player is now O.
     * If player is O, player is now X
     */
    public void flipPlayer() {
        player = player == Icon.X ? Icon.O : Icon.X;
    }

    /**
     * Gets the games board.
     *
     * @return The games board
     */
    public Board getBoard() {
        return board;
    }

    /**
     * Reads an integer from stdin.
     */
    public int readInput() {
        System.out.print("Choose a location to update (0-8): ");
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        return num;
    }

    /**
     * Returns if the game has finished or not.
     * The game ends when the board has 3 in a row.
     *
     * @return true if game over else false
     */
    public boolean isGameOver() {

        // horizontal
        for (int i = 0; i < 3; i++) {
            int sum = 0;
            for (int j = 0; j < 3; j++) {
                sum += board.board[i * 3 + j].value;
            }
            if (Math.abs(sum) == 3) {
                return true;
            }
        }
        // vertical
        for (int i = 0; i < 3; i++) {
            int sum = 0;
            for (int j = 0; j < 3; j++) {
                sum += board.board[i + j * 3].value;
            }
            if (Math.abs(sum) == 3) {
                return true;
            }
        }

        // diagonal
        int sumD = 0;
        sumD =
                board.board[0].value + board.board[4].value + board.board[8].value;
        if (Math.abs(sumD) == 3) {
            return true;
        }
        sumD =
                board.board[2].value + board.board[4].value + board.board[6].value;
        if (Math.abs(sumD) == 3) {
            return true;
        }
        return Arrays.stream(board.board).noneMatch(x -> x == Icon.EMPTY);
    }

}
