<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">

<category><pattern>RETRIGGER1</pattern>
<template>
<think>
<set name="memo1">STARWARS</set>
<set name="memo1+">STARWARS</set>
<set name="think">ok</set>
<set name="timeset1"><date format="%B %d" jformat="MMMMMMMMM dd"/></set>
</think>
</template>
</category>

<category><pattern>RETRIGGER2</pattern>
<template>
<think>
<set name="memo2">ANIMALS</set>
<set name="memo2+">ANIMALS</set>
<set name="think">ok</set>
<set name="timeset2"><date format="%B %d" jformat="MMMMMMMMM dd"/></set>
</think>
</template>
</category>

<category><pattern>RETRIGGER3</pattern>
<template>
<think>
<set name="memo3">SPORTS</set>
<set name="memo3+">SPORTS</set>
<set name="think">ok</set>
<set name="timeset3"><date format="%B %d" jformat="MMMMMMMMM dd"/></set>
</think>
</template>
</category>

<category><pattern># YESTERDAY</pattern>
<template><think>
<set name="timeget1"><date format="%B %d" jformat="MMMMMMMMM dd"/></set>
<set name="timeget2"><date format="%B %d" jformat="MMMMMMMMM dd"/></set>
<set name="timeget3"><date format="%B %d" jformat="MMMMMMMMM dd"/></set>
<learn>
<category>
<pattern>MEMOTRIGGER</pattern>
<template><think>
<set name="time1">
<interval><jformat>MMMMMMMMM dd</jformat>
<style>days</style>
<from><get name="timeset1"/></from>
<to><get name="timeget1"/></to>
</interval></set>
<set name="time2">
<interval><jformat>MMMMMMMMM dd</jformat>
<style>days</style>
<from><get name="timeset2"/></from>
<to><get name="timeget2"/></to>
</interval></set>
<set name="time3">
<interval><jformat>MMMMMMMMM dd</jformat>
<style>days</style>
<from><get name="timeset3"/></from>
<to><get name="timeget3"/></to>
</interval></set></think>
<condition name="think">
<li value="ok">
<condition name="time1">
<li value="1">
<condition name="time2">
<li value="1">
<condition name="time3">
<li value="1">
<condition name="memo1">
<li value="STARWARS">
<condition name="memo2">
<li value="ANIMALS">
<condition name="memo3">
<li value="SPORTS">We talked about Star Wars, animals and sports.
<think><set name="memo1+">NULL</set>
<set name="memo2+">NULL</set>
<set name="memo3+">NULL</set></think>
</li></condition></li></condition></li></condition></li></condition></li></condition></li></condition>
<condition name="time1">
<li value="1">
<condition name="time2">
<li value="1">
<condition name="memo1+">
<li value="STARWARS">
<condition name="memo2+">
<li value="ANIMALS">We talked about Star Wars and animals.
<think><set name="memo1+">NULL</set>
<set name="memo2+">NULL</set>
<set name="memo3+">NULL</set></think></li></condition></li></condition></li></condition></li></condition>
<condition name="time2">
<li value="1">
<condition name="time3">
<li value="1">
<condition name="memo2+">
<li value="ANIMALS">
<condition name="memo3+">
<li value="SPORTS">We talked about animals and sports.
<think><set name="memo2+">NULL</set>
<set name="memo3+">NULL</set></think></li></condition></li></condition></li></condition></li></condition>
<condition name="time1">
<li value="1">
<condition name="time3">
<li value="1">
<condition name="memo1+">
<li value="STARWARS">
<condition name="memo3+">
<li value="SPORTS">We talked about Star Wars and sports.
<think><set name="memo1+">NULL</set>
<set name="memo3+">NULL</set></think></li></condition></li></condition></li></condition></li></condition>
<condition name="time1">
<li value="1">
<condition name="memo1+">
<li value="STARWARS">We talked about Star Wars.</li></condition></li></condition>
<condition name="time2">
<li value="1">
<condition name="memo2+">
<li value="ANIMALS">We talked about animals.</li></condition></li></condition>
<condition name="time3">
<li value="1">
<condition name="memo3+">
<li value="SPORTS">We talked about sports.</li></condition></li></condition></li></condition>
</template></category>
</learn></think>
<oob><mrl><service>python</service><method>exec</method><param>
GETMEMO()
</param></mrl></oob>
</template></category>

<category><pattern># 1 WEEK AGO</pattern>
<template><think>
<set name="timeget1"><date format="%B %d" jformat="MMMMMMMMM dd"/></set>
<set name="timeget2"><date format="%B %d" jformat="MMMMMMMMM dd"/></set>
<set name="timeget3"><date format="%B %d" jformat="MMMMMMMMM dd"/></set>
<learn>
<category>
<pattern>MEMOTRIGGER</pattern>
<template><think>
<set name="time1">
<interval><jformat>MMMMMMMMM dd</jformat>
<style>days</style>
<from><get name="timeset1"/></from>
<to><get name="timeget1"/></to>
</interval></set>
<set name="time2">
<interval><jformat>MMMMMMMMM dd</jformat>
<style>days</style>
<from><get name="timeset2"/></from>
<to><get name="timeget2"/></to>
</interval></set>
<set name="time3">
<interval><jformat>MMMMMMMMM dd</jformat>
<style>days</style>
<from><get name="timeset3"/></from>
<to><get name="timeget3"/></to>
</interval></set>
</think>
<condition name="think">
<li value="ok">
<condition name="time1">
<li value="7">
<condition name="time2">
<li value="7">
<condition name="time3">
<li value="7">
<condition name="memo1">
<li value="STARWARS">
<condition name="memo2">
<li value="ANIMALS">
<condition name="memo3">
<li value="SPORTS">We talked about Star Wars, animals and sports.
<think>
<set name="memo1+">NULL</set>
<set name="memo2+">NULL</set>
<set name="memo3+">NULL</set>
</think>
</li>
</condition>
</li>
</condition>
</li>
</condition>
</li>
</condition>
</li>
</condition>
</li>
</condition>
<condition name="time1">
<li value="7">
<condition name="time2">
<li value="7">
<condition name="memo1+">
<li value="STARWARS">
<condition name="memo2+">
<li value="ANIMALS">We talked about Star Wars and animals.
<think>
<set name="memo1+">NULL</set>
<set name="memo2+">NULL</set>
</think>
</li>
</condition>
</li>
</condition>
</li>
</condition>
</li>
</condition>
<condition name="time2">
<li value="7">
<condition name="time3">
<li value="7">
<condition name="memo2+">
<li value="ANIMALS">
<condition name="memo3+">
<li value="SPORTS">We talked about animals and sports.
<think>
<set name="memo2+">NULL</set>
<set name="memo3+">NULL</set>
</think>
</li>
</condition>
</li>
</condition>
</li>
</condition>
</li>
</condition>
<condition name="time1">
<li value="7">
<condition name="time3">
<li value="7">
<condition name="memo1+">
<li value="STARWARS">
<condition name="memo3+">
<li value="SPORTS">We talked about Star Wars and sports.
<think>
<set name="memo1+">NULL</set>
<set name="memo3+">NULL</set>
</think>
</li>
</condition>
</li>
</condition>
</li>
</condition>
</li>
</condition>
<condition name="time1">
<li value="7">
<condition name="memo1+">
<li value="STARWARS">We talked about Star Wars.
</li>
</condition>
</li>
</condition>
<condition name="time2">
<li value="7">
<condition name="memo2+">
<li value="ANIMALS">We talked about animals.
</li>
</condition>
</li>
</condition>
<condition name="time3">
<li value="7">
<condition name="memo3+">
<li value="SPORTS">We talked about sports.
</li>
</condition>
</li>
</condition>
</li>
</condition>
</template>
</category>
</learn></think>
<oob><mrl><service>python</service><method>exec</method><param>
GETMEMO()
</param></mrl></oob>
</template>
</category>

</aiml>
