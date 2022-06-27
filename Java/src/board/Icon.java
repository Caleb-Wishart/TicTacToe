package board;

/**
 * An Icon on the board.
 */
public enum Icon {
    X("X",1),
    O("O",-1),
    EMPTY(" ",0);

    /**
     * The string form of the Icon
     */
    private String representation;

    /**
     * The value of that icon for magic squares.
     */
    public int value;

    /**
     * Creates an icon
     * @param representation the string form of the Icon
     * @param value the value of that icon.
     */
    Icon(String representation, int value){
        this.representation = representation;
        this.value = value;
    }

    /**
     * Returns the human-readable string representation of this Icon.
     * @return human-readable string
     */
    @Override
    public String toString() {
        return representation;
    }
}
