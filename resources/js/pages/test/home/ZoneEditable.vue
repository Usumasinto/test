<template>
  <div class="zone-editable">
    
    <div
      v-if="display"
      class="zone-display"
      
    >
    
    
      <div>
        Zone Name: <strong>{{ name }}</strong> Distributions: {{ distributionDisplay }} 
       
      </div>
      

      <button
        class="btn btn-primary"
        @click="setDisplay(false)"
        :disabled="saving"
      >
        Edit
      </button>
      <button
        class="btn btn-secondary"
        @click="remove"
        :disabled="saving"
      >
        Delete
      </button>
    </div>
    
    <div
      v-else
      class="zone-edit"
    >
      <label class="control-label">
        Zone Name
      </label>

      <input
        v-model="form.name"
        placeholder="Zone name"
        class="form-control"
        :disabled="saving"
        required
      >

      <div class="zone-edit-distributions">
        <div v-for="(distribution) in form.distributions" v-bind:key="distribution.id">
          <label class="control-label">
            Distribution
          </label>

          <input
            v-model="distribution.percentage" 
            placeholder="Percentage"
            class="form-control"
            
          >
          
        </div>
        
      </div>

      <div class="zone-edit-actions">
        <button
          class="btn btn-secondary"
          @click="setCancel(true)"
          :disabled="saving"
        >
         Cancel
        </button>

        <button
          class="btn btn-success"
          @click="save"
          :disabled="saving"
        >
          Save
        </button>
        
      </div>
      
    </div>
    
  </div>
  
  
</template>

<script>
export default {
  name: 'ZoneEditable',
  props: {
    name: String,
    id: Number,
    distributions: Array,
  },
  data() {
    return {
      display: true,
      form: {
        name: '',
        distributions: [],
      },
      saving: false,
    };
  },
  computed: {
    distributionDisplay() {
      let percent = "%";
      return this.distributions.map(distribution => distribution.percentage + percent ).join( '-' );
    }
  },
  mounted() {
    this.getValuesFromProps();
  },
  methods: {
    getValuesFromProps() {
      this.form.name = this.name;
      this.form.distributions = this.distributions.map(distribution => {
        return {
          id: distribution.id,
          percentage: distribution.percentage 
        };
      });
    },
    setDisplay(value) {
      this.display = value;
      if(!this.display) {
        this.getValuesFromProps();
      }
    },

    //method to activate CANCEL button
     setCancel(value) {
      this.display = value;
      if(this.display) {
        this.display=true
      }
    },
    //

    async remove(){

      const paramsRemove = {
        id: this.id,
        name: this.form.name,
          
      };
      axios.delete(`/api/zones/delete-zone/${paramsRemove.id}`)
      .then(()=> {alert("Zone deleted! ");});



      

    },
    
    async save() {
      this.saving = true;

      const params = {
        id: this.id,
        name: this.form.name,
        distributions: this.form.distributions,

      };
        try{
          if (params.name == ''){
            alert("You cannot leave the zone name empty")
            this.saving = false;
          }else {

            await axios.put('/api/zones/edit-update/' , params ).then(() => {alert('Zone has been changed'); });



            this.$emit('edit', {name: params.name , distributions: params.distributions});

      
            this.saving = false;
            this.display = false;

          } 
        }catch(error){
          alert("there was an error")
        }
    
    }
  }
}
</script>

<style lang="scss">
@import 'resources/scss/variables.scss';

.zone-editable {
  border: 1px solid $gray-color;
  padding: $qmb;
  border-radius: $border-radius;

  .zone-display {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .zone-edit {
    display: flex;
    flex-direction: column;
    gap: $small-action-space;

    .zone-edit-actions {
      display: flex;
      gap: $small-action-space;
      justify-content: end;
    }

    .zone-edit-distributions {
      display: grid;
      grid-template-columns: repeat(1, 1fr);
      gap: $small-action-space;
    }
  }
}
</style>
