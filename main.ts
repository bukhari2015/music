input.onButtonPressed(Button.A, function () {
    music.play(music.stringPlayable("F G F E G E F G ", 120), music.PlaybackMode.LoopingInBackground)
})
input.onButtonPressed(Button.AB, function () {
    music.play(music.stringPlayable("E B C5 A B G A F ", 120), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    music.stopAllSounds()
})
