<template>
  <div class="profile-box" style="flex: 0 1 400px;">
    <h1>{{ user.username }}</h1>
    <div class="details-box flex-row">
      <span class="profile-picture">
        <img width="150" src="https://placehold.it/100">
      </span>
      <div class="flex-col">
       <span class="age">{{ user.age }} years old</span>
       <span class="gender">{{ user.gender }}</span>
       <span class="country">{{ user.country }}</span>       
     </div>
   </div>
   <div class="contact-user bordered">
    <span class="flex-row p-0">
      <ul class="p-0 w-50"> 
        <li class="p-0 m-0"><button href="#">Block User</button></li>
        <li class="p-0 m-0"><button href="#">Report User</button></li>
      </ul>
      <ul class="p-0 w-50">
        <li class="p-0 m-0"><button href="#">Send Friend Request</button></li>
      </ul>
    </span>
   </div>
   <div class="pyspace-url bordered">
    <p class="font-weight-bold m-0">PySpace Url :</p>
    <a href="#">https://pyspace.net/?id={{ user.id }}</a>
   </div>
   <div class="user-profile-track alert-dark bordered p-0">
    <p class="m-0 p-0"><b>Song:</b> Friends – I'll Be There For You</p>
     <audio controls class="m-0" style="width: 100%;"></audio>
   </div>
 </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'UserProfile',
  props: ['user'],
};

</script>
