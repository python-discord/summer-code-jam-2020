<template>
  <div class="tic-tac-toe-container">
    <div class="tictactoe-board">
      <div v-for="(item, index) in board" class="board-item" :class="`board-${index}`">
        <span class="board-move">{{item}}</span>
        <span class="board-number">{{index}}</span>
      </div>
    </div>
    <div class="tic-tac-toe-banner" v-if="isOver">
      <div v-if="score === 0">
        Draw
      </div>
      <div v-else-if="score === 1">
        You won!
      </div>
      <div v-else>
        git gud scrub
      </div>
    </div>
  </div>
</template>

<style>
.tic-tac-toe-banner {
  margin-top: 1em;
}

.tic-tac-toe-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.tictactoe-board {
  display: grid;
  grid-template-rows: 1fr 1fr 1fr;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 0;
  width: 13em;
  align-content: center;
  align-self: center;
  justify-content: center;
}

.board-item {
  height: 3em;
  padding: 1em;
  width: 3em;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20pt;
  position: relative;
}

.board-number {
  font-size: 10pt;
  position: absolute;
  bottom: 0;
}

/* Cell specific styling */
.board-0,
.board-3,
.board-6{
  border-right: 1px solid var(--font-color);
}

.board-3,
.board-4,
.board-5{
  border-top: 1px solid var(--font-color);
  border-bottom: 1px solid var(--font-color);
}

.board-2,
.board-5,
.board-8{
  border-left: 1px solid var(--font-color);
}

</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      board: [
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
        null,
      ],
      player: 'X',
      isOver: false,
      score: 0,
    };
  },
  mounted() {
    this.getMove();
    this.$cmd.on('/exit', () => this.$router.push('/'), 'Exit the game');
  },
  methods: {
    makeMove(move) {
      axios.post('/api/games/ttt', {
        player: this.player,
        board: this.board,
        move,
      }).then((res) => {
        this.board = res.data.board;
        this.isOver = res.data.game_over;
        this.score = res.data.score;
        if (!this.isOver) {
          this.getMove();
        }
      });
    },
    getMove() {
      this.$cmd.input('Move (0-8): ').then((move) => {
        if (move === '/exit') {
          return;
        }
        if (isNaN(move) || +move < 0 || +move > 8) {
          this.getMove();
        } else {
          this.makeMove(Number(move));
        }
      });
    },
  },
};
</script>
