public enum Direction {
    NORTH,
    EAST,
    SOUTH,
    WEST;


    public Direction turnLeft() {
        switch(this) {
            case NORTH:
                return Direction.WEST;
            case EAST:
                return Direction.NORTH;
            case SOUTH:
                return Direction.EAST;
            case WEST:
                return Direction.SOUTH;
            default:
                return null;
        }
    }


    public Direction turnRight() {
        switch(this) {
            case NORTH:
                return Direction.EAST;
            case EAST:
                return Direction.SOUTH;
            case SOUTH:
                return Direction.WEST;
            case WEST:
                return Direction.NORTH;
            default:
                return null;
        }
    }


    public Direction turnBack() {
        switch(this) {
            case NORTH:
                return Direction.SOUTH;
            case EAST:
                return Direction.WEST;
            case SOUTH:
                return Direction.NORTH;
            case WEST:
                return Direction.EAST;
            default:
                return null;
        }
    }
}
