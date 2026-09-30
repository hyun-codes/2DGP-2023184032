"""과제 재생 조건 검증. 이미지 추가 라이브러리는 필요하지 않다."""

import unittest
from types import SimpleNamespace
from unittest.mock import patch

import animation_viewer as viewer


class ViewerTests(unittest.TestCase):
    def test_rectangles_and_enlargement(self):
        for name, frames, _ in viewer.ANIMATIONS:
            for frame in frames:
                with self.subTest(action=name, frame=frame):
                    left, top, width, height = frame
                    self.assertGreaterEqual(left, 0)
                    self.assertGreaterEqual(top, 0)
                    self.assertLessEqual(left + width, 2100)
                    self.assertLessEqual(top + height, 1325)
                    self.assertGreaterEqual(height * viewer.DRAW_SCALE, 300)
                    self.assertLessEqual(width * viewer.DRAW_SCALE, 800)
                    self.assertLessEqual(height * viewer.DRAW_SCALE, 600)
                    clip = viewer.to_clip_rectangle(frame, 1325)
                    self.assertEqual(1325 - clip[1] - clip[3], top)

    def test_bonus_conditions(self):
        self.assertGreaterEqual(len(viewer.ANIMATIONS), 4)
        self.assertGreater(len({len(frames) for _, frames, _ in viewer.ANIMATIONS}), 1)
        for _, frames, _ in viewer.ANIMATIONS:
            self.assertGreater(len({frame[2:] for frame in frames}), 1)

    def test_five_cycles_then_one_second_hold(self):
        for animation in viewer.ANIMATIONS:
            _, frames, duration = animation
            with patch.object(viewer, 'show_frame_for', return_value=True) as show:
                self.assertTrue(viewer.play_animation(None, animation))
                calls = [(c.args[1], c.args[2]) for c in show.call_args_list]
                expected = [(f, duration) for f in frames] * 5
                expected.append((frames[-1], 1.0))
                self.assertEqual(calls, expected)

    def test_exit_interrupts_frame_and_pause(self):
        for duration in (0.14, 1.0):
            with patch.object(viewer, 'handle_events', return_value=False):
                with patch.object(viewer, 'draw_frame') as draw:
                    self.assertFalse(viewer.show_frame_for(None, viewer.IDLE_FRAMES[0], duration))
                    draw.assert_not_called()

    def test_escape_and_close(self):
        events = (
            SimpleNamespace(type=viewer.SDL_QUIT),
            SimpleNamespace(type=viewer.SDL_KEYDOWN, key=viewer.SDLK_ESCAPE),
        )
        for event in events:
            with patch.object(viewer, 'get_events', return_value=[event]):
                self.assertFalse(viewer.handle_events())

    def test_whole_sequence_wraps_and_closes(self):
        calls = []

        def play(_, animation):
            calls.append(animation[0])
            return len(calls) < len(viewer.ANIMATIONS) + 1

        with patch.object(viewer, 'open_canvas'), patch.object(viewer, 'load_image'):
            with patch.object(viewer, 'play_animation', side_effect=play):
                with patch.object(viewer, 'close_canvas') as close:
                    viewer.main()
                    close.assert_called_once()
        names = [a[0] for a in viewer.ANIMATIONS]
        self.assertEqual(calls, names + names[:1])


if __name__ == '__main__':
    unittest.main()
