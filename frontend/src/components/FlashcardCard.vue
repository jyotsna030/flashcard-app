<template>
  <div class="group w-full max-w-xs">
    <!-- Card container with perspective and hover lift -->
    <div
      class="relative w-full h-40 [perspective:1000px] cursor-pointer"
      @click="flipped = !flipped"
    >
      <div
        :class="[
          'relative w-full h-full transition-transform duration-500 ease-in-out [transform-style:preserve-3d]',
          flipped ? '[transform:rotateY(180deg)]' : ''
        ]"
      >
        <!-- FRONT FACE -->
        <div
          :style="cardStyle(colorIndex)"
          class="absolute inset-0 p-6 rounded-lg shadow-md transition-shadow duration-300 [backface-visibility:hidden] group-hover:shadow-xl"
        >
          <p class="font-semibold">{{ card.question }}</p>
          <div class="mt-auto text-sm opacity-75">{{ card.tag }}</div>
          <!-- Shine overlay -->
          <div
            class="absolute top-0 left-0 w-full h-full pointer-events-none bg-gradient-to-r from-white/0 via-white/20 to-white/0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 [transform:rotate(25deg)] origin-top-left"
          ></div>
        </div>

        <!-- BACK FACE -->
        <div
          :style="cardStyle(colorIndex)"
          class="absolute inset-0 p-6 rounded-lg shadow-md transition-shadow duration-300 [transform:rotateY(180deg)] [backface-visibility:hidden] group-hover:shadow-xl"
        >
          <p class="font-semibold mb-2">Answer:</p>
          <p>{{ card.answer }}</p>
          <!-- Shine overlay -->
          <div
            class="absolute top-0 left-0 w-full h-full pointer-events-none bg-gradient-to-r from-white/0 via-white/20 to-white/0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 [transform:rotate(25deg)] origin-top-left"
          ></div>
        </div>
      </div>
    </div>

    <!-- Delete button -->
    <button
      class="mt-2 text-red-500 hover:text-red-400 text-sm opacity-0 group-hover:opacity-100 transition-opacity duration-200"
      @click.stop="deleteCard"
    >
      Delete
    </button>
  </div>
</template>

<script>
export default {
  props: ['card', 'colorIndex'],
  data() {
    return { flipped: false }
  },
  methods: {
    cardStyle(index) {
      const palette = [
        '#89AC46', '#FFD95F', '#497D74', '#B82132', '#FE4365',
        '#7F55B1', '#FF9B17', '#9F5255'
      ];
      const textColors = [
        '#2A363B', '#2A363B', '#FFFFFF', '#FFFFFF', '#FFFFFF',
        '#FFFFFF', '#2A363B', '#FFFFFF'
      ];
      const bg = palette[index % palette.length];
      const text = textColors[index % textColors.length];
      return {
        backgroundColor: bg,
        color: text,
      };
    },
    async deleteCard() {
      await fetch(
        `http://127.0.0.1:8000/api/flashcards/${this.card.id}/`,
        { method: 'DELETE' }
      )
      this.$emit('deleted', this.card.id)
    },
  },
}
</script>
