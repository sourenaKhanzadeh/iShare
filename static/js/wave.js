/**
 * Created by Owner on 5/23/2019.
 */

// get canvas
const canvas = document.querySelector('canvas');
const c = canvas.getContext('2d');

// set Canvas size
canvas.width = innerWidth;
canvas.height = innerHeight;

// resize the window
window.addEventListener('resize',()=>{
    // set Canvas size
    canvas.width = innerWidth;
    canvas.height = innerHeight;
});

// make wave object
const Wave = {
  y:canvas.height-200,
  length: 0.01,
  amplitude:70,
  frequency:0.01,
  increase_freq:1,
  flag : true,
  color:'#E87551',
  draw:function () {
    c.clearRect(0, 0, canvas.width, canvas.height);
    c.beginPath();
    c.moveTo(0, this.y);

    // create the wave the wave
    for(let i=0;i<canvas.width;i++){
        c.lineTo(i, this.y +
            Math.sin(i *this.length + this.increase_freq)
            * this.amplitude)

    }
    c.strokeStyle = this.color;
    c.stroke();

    c.closePath();
    //create the rectangle

  },
  update:function () {
      // draw the wave then update it
      this.draw();
      // move the object
      this.movement();
  },
  movement:function () {
      this.increase_freq += this.frequency;
      velocity = 2;
      this.frequency += 0.001;

      // organize frequency
      if(this.frequency > 0.5){
          this.frequency = 0.001
      }
      // create a wave form
      if(this.flag){
          this.amplitude -= velocity;
          if(this.amplitude < -70){
              this.flag = false;

          }
      }else{
          this.amplitude += velocity;
          if(this.amplitude > 70){
              this.flag = true;
          }

      }

  }

};

// make a scene and add all game objects
scene = [Wave];

// start animation
function animate() {
    requestAnimationFrame(animate);

    // update all game objects in the scene
    for(gameobject of scene){
        gameobject.update();
    }


}

animate();