<template>
  <div class="min-h-screen text-black p-6 relative overflow-hidden bg-radial-pattern">
    <!-- Typing‑Animation Heading -->
    <h1
      class="font-poppins text-4xl font-extrabold text-center mb-6 text-blue-700"
    >
      {{ displayText }}
      <span
        v-if="cursorVisible"
        class="inline-block w-1 h-8 bg-blue-700 animate-blink"
      ></span>
    </h1>

    <!-- Spacer -->
    <div class="h-12"></div>

    <!-- Form Panel -->
    <transition name="slide-down">
      <form
        v-if="showForm"
        @submit.prevent="addFlashcard"
        class="bg-white p-6 rounded-lg shadow-xl max-w-md w-full mx-auto mb-6"
      >
        <h2 class="text-2xl mb-4 font-semibold text-gray-800">
          New Flashcard
        </h2>
        <input
          v-model="newCard.question"
          placeholder="Question"
          class="w-full p-2 rounded border mb-3 focus:ring-2 focus:ring-blue-400"
          required
        />
        <input
          v-model="newCard.answer"
          placeholder="Answer"
          class="w-full p-2 rounded border mb-3 focus:ring-2 focus:ring-blue-400"
          required
        />
        <input
          v-model="newCard.tag"
          placeholder="Tag (optional)"
          class="w-full p-2 rounded border mb-3 focus:ring-2 focus:ring-blue-400"
        />
        <button
          type="submit"
          class="w-full py-2 bg-green-600 text-white rounded hover:bg-green-500 transition"
        >
          Save
        </button>
      </form>
    </transition>

    <!-- Flashcards Grid -->
    <div
      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 justify-items-center"
    >
      <!-- Existing Flashcards -->
      <FlashcardCard
        v-for="(card, i) in flashcards"
        :key="card.id"
        :card="card"
        :color-index="i"
        @deleted="removeFlashcard"
      />

      <!-- Card Placeholder -->
      <div
        v-if="!showForm"
        @click="showForm = true"
        class="box-border w-[220.4px] h-[160px] p-6 flex items-center justify-center cursor-pointer rounded-lg shadow-lg bg-blue-600 hover:bg-blue-700 transition"
      >
        <span class="text-5xl text-white">+</span>
      </div>
      <div
        v-else
        @click="showForm = false"
        class="box-border w-[220.4px] h-[160px] p-6 flex items-center justify-center cursor-pointer rounded-lg shadow-lg bg-blue-600 hover:bg-blue-700 transition"
      >
        <span class="text-5xl text-white">&times;</span>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import FlashcardCard from './components/FlashcardCard.vue'

export default {
  components: { FlashcardCard },
  setup() {
    const flashcards = ref([])
    const newCard = ref({ question: '', answer: '', tag: '' })
    const showForm = ref(false)

    // Typewriter state
    const messages = [
      'Flashcard App',
      'that lets you add, flip and delete flashcards',
      'made with Vue.js and Django',
    ]
    const displayText = ref('')
    const cursorVisible = ref(true)

    let msgIndex = 0
    let charIndex = 0
    let typing = true

    const typeSpeed = 100
    const pauseAfter = 1500

    function tick() {
      const current = messages[msgIndex]
      if (typing) {
        if (charIndex < current.length) {
          displayText.value += current[charIndex++]
          setTimeout(tick, typeSpeed)
        } else {
          typing = false
          setTimeout(tick, pauseAfter)
        }
      } else {
        if (charIndex > 0) {
          displayText.value = current.slice(0, --charIndex)
          setTimeout(tick, typeSpeed / 2)
        } else {
          typing = true
          msgIndex = (msgIndex + 1) % messages.length
          setTimeout(tick, typeSpeed)
        }
      }
    }

    // Blink cursor
    setInterval(() => {
      cursorVisible.value = !cursorVisible.value
    }, 500)

    const fetchFlashcards = async () => {
      const res = await fetch('http://127.0.0.1:8000/api/flashcards/')
      flashcards.value = await res.json()
    }

    const addFlashcard = async () => {
      await fetch('http://127.0.0.1:8000/api/flashcards/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newCard.value),
      })
      newCard.value = { question: '', answer: '', tag: '' }
      showForm.value = false
      fetchFlashcards()
    }

    const removeFlashcard = (deletedId) => {
      flashcards.value = flashcards.value.filter((c) => c.id !== deletedId)
    }

    onMounted(() => {
      tick()
      fetchFlashcards()
    })

    return {
      flashcards,
      newCard,
      showForm,
      addFlashcard,
      removeFlashcard,
      displayText,
      cursorVisible,
    }
  },
}
</script>


