package board;

import java.util.Arrays;
import java.util.stream.Collectors;

/**
 * The board that the game takes place on.
 */
public class Board {
    public Icon[] board;

    /**
     * Creates a new Board.
     * Constructs a new array of Icons, each item is set to EMPTY.
     */
    public Board(){
        this.board = new Icon[9];
        Arrays.fill(board, Icon.EMPTY);
    }

    /**
     * Updates a position on the board
     * @param icon the icon to be changed
     * @param index the index to change
     * @throws IndexOutOfBoundsException if index < 0 || index > 8
     * @throws IllegalArgumentException if \old(board)[index] != EMPTY
     */
    public void update(Icon icon, int index)
            throws IndexOutOfBoundsException, IllegalArgumentException {
        if(index < 0 || index > 8){
            throw new IndexOutOfBoundsException("Index not on the board");
        }
        if(this.board[index] != Icon.EMPTY){
            throw new IllegalArgumentException("State has not changed");
        }
        this.board[index] = icon;
    }


    /**
     * The board guide to draw on the CLI.
     * The format to be shown is:
     * <pre>
     *     0 | 1 | 2
     *    -----------
     *     3 | 4 | 5
     *    -----------
     *     6 | 7 | 8
     * </pre>
     * @return CLI version of the board guide.
     */
    public static String drawGuide(){
        return  String.format("0 | 1 | 2 %n" +
                "-----------%n" +
                "3 | 4 | 5 %n" +
                "-----------%n" +
                "6 | 7 | 8 ");
    }

    /**
     * The board to draw on the CLI.
     * The format to be shown is:
     * <pre>
     *     0 | 1 | 2
     *    -----------
     *     3 | 4 | 5
     *    -----------
     *     6 | 7 | 8
     * </pre>
     * Where {@code 0-8} is the string representation of the ICON at that index
     * in the board.
     * <br> For example:
     * <pre>
     *     X | O |
     *    -----------
     *     X |   | O
     *    -----------
     *       |   |
     * </pre>
     * @return CLI version of this board.
     */
    public String drawBoard(){
        return String.format(
                " %s | %s | %s %n" +
                "-----------%n" +
                " %s | %s | %s %n" +
                "-----------%n" +
                " %s | %s | %s ",
                (Object[]) this.board
        );
    }

    /**
     * The human-readable representation of this board.
     * The format to be shown is:
     * <pre>Board: icons</pre>
     * Where {@code icons} is a comma separated list of the bord state.
     * <br> For example:
     * <pre>Board: X,O, ,X, ,O, , , </pre>
     * @return human-readable version of this board.
     */
    public String toString(){
        return "Board: "
                + Arrays.stream(this.board)
                .map(Icon::toString)
                .collect(Collectors.joining(","));
    }

}
