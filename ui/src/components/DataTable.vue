// frontend/src/components/DataTable.vue
<template>

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="user in tableData" :key="user.id">
      <td>{{ user.id }}</td>
      <td>{{ user.username }}</td>
      <td>{{ user.email }}</td>
    </tr>
  </tbody>
</table>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tableData: [
      ]
    };
  },
  mounted() {
    axios.get('http://localhost:5000/users') // Adjust if needed
      .then(response => {
        this.tableData = response.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  },
};
</script>
