<template>
  <input type="file" @change="handleFileChange" />
  <button @click="uploadFile">Upload</button>
  <div v-if="response">
    <div>{{ response }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedFile: null,
      response: null,
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    async uploadFile() {
      if (!this.selectedFile) {
        this.response = "File Empty"
        return ;
      }

      const formData = new FormData();
      formData.append('file', this.selectedFile);

      try {
        const response = await axios.post('http://localhost:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('Upload successful:', response.data);
        this.response = "File Uploaded";
      } catch (error) {
        console.error('Upload failed:', error);
      }
    },
  },
};
</script>
